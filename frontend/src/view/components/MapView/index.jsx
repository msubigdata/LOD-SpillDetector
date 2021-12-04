/* eslint-disable max-len */
import React, { Fragment, useEffect, useState } from 'react';
import MarkerClusterGroup from 'react-leaflet-markercluster';
import Slider from '@mui/material/Slider';
import PropTypes from 'prop-types';
import {
    MapContainer,
    TileLayer,
    ZoomControl,
    ScaleControl,
    Marker,
    Rectangle,
    ImageOverlay,
    Popup,
} from 'react-leaflet';
import markerIcon from 'assets/icons/marker-alert.svg';
import markerIconG from 'assets/icons/marker-alert-green.svg';
import markerIconY from 'assets/icons/marker-alert-yellow.svg';
import markerIconO from 'assets/icons/marker-alert-orange.svg';
import L from 'leaflet';
import './styleFix';
import './styles/main.scss';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faWater, faHome, faRoad } from '@fortawesome/free-solid-svg-icons';

const southWest = L.latLng(-90, -200);
const northEast = L.latLng(90, 200);
const bounds = L.latLngBounds(southWest, northEast);

export const MapView = ({ markers, activeReg, mapRef, setMapRef }) => {
    const [markerData, setMarkerData] = useState(markers);
    const badgeIcons = {
        water: faWater,
        home: faHome,
        road: faRoad,
    };

    const [inspectBadge, setInspectBadge] = useState([]);

    const inspectArea = async (area) => {
        const { data } = await axios.post('/api/v1/inspect/', {
            bbox: area,
        });

        setInspectBadge([...data]);
    };

    useEffect(() => {
        setMarkerData(markers);
    }, [markers]);

    useEffect(() => {
        if (activeReg.lat && activeReg.long && mapRef) {
            mapRef.setView([activeReg.lat, activeReg.long], 14);
        }
    }, [activeReg, mapRef]);

    const MapMarker = ({ marker, timestamps }) => {
        const freshImg = timestamps[timestamps.length - 1];

        const [date, setDate] = useState(freshImg.timestamp);

        function closest(x, arr) {
            return arr.find((d) => d.timestamp >= x) || arr[arr.length - 1];
        }

        const ico = () => {
            if (marker.color === 'red') {
                return markerIcon;
            }
            if (marker.color === 'green') {
                return markerIconG;
            }
            if (marker.color === 'orange') {
                return markerIconO;
            }
            return markerIconY;
        };

        const markerIco = L.icon({
            iconUrl: ico(),
            iconAnchor: [14, 40],
            popupAnchor: [0, -100],
            iconSize: [28, 40],
        });

        return (
            <>
                <Rectangle
                    fill={false}
                    bounds={marker.area[0]}
                    pathOptions={{ color: marker.color }}
                />
                <ImageOverlay
                    bounds={marker.area[0]}
                    url={closest(date, timestamps).url || ''}
                />
                <Marker
                    eventHandlers={{
                        click: () => {
                            mapRef.setView(
                                [
                                    (marker.area[0][1][0] +
                                        marker.area[0][0][0]) /
                                        2,
                                    (marker.area[0][1][1] +
                                        marker.area[0][0][1]) /
                                        2,
                                ],
                                14
                            );
                        },
                    }}
                    icon={markerIco}
                    position={[
                        (marker.area[0][1][0] + marker.area[0][0][0]) / 2,
                        (marker.area[0][1][1] + marker.area[0][0][1]) / 2,
                    ]}
                >
                    <Popup className="popup" style={{ opacity: '0.3' }}>
                        <div className="slider_wrapper">
                            <h6>
                                {new Date(date * 1000).toLocaleDateString()}
                            </h6>
                            <Slider
                                aria-label="Custom marks"
                                defaultValue={date}
                                value={date}
                                step={86400}
                                min={timestamps[0]?.timestamp}
                                max={
                                    timestamps[timestamps.length - 1]?.timestamp
                                }
                                onChange={(e, v) => setDate(v)}
                                valueLabelDisplay="off"
                                marks={timestamps?.map((t) => {
                                    return {
                                        value: t.timestamp,
                                    };
                                })}
                            />
                            <div className="justify-content-center d-flex">
                                <FontAwesomeIcon
                                    icon={faWater}
                                    color="#489be5"
                                    style={{
                                        fontSize: '25px',
                                        margin: '10px',
                                    }}
                                />
                            </div>
                        </div>
                    </Popup>
                </Marker>
            </>
        );
    };

    MapMarker.propTypes = {
        marker: PropTypes.oneOfType([PropTypes.any]).isRequired,
        timestamps: PropTypes.oneOfType([PropTypes.any]),
    };

    MapMarker.defaultProps = {
        timestamps: [],
    };

    return (
        <>
            <MapContainer
                center={[55.754093, 37.620407]}
                zoom={3}
                minZoom={3}
                zoomControl={false}
                maxBounds={bounds}
                attributionControl={false}
                whenCreated={setMapRef}
                preferCanvas
            >
                <TileLayer url="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" />
                <MarkerClusterGroup>
                    {markerData?.map((m, i) => {
                        const timestamps = [
                            ...new Map(
                                m?.images?.map((v) => [v.timestamp, v])
                            ).values(),
                        ]?.sort((a, b) => a.timestamp - b.timestamp);

                        return (
                            <MapMarker
                                marker={m}
                                timestamps={timestamps}
                                key={`${i + 1}`}
                            />
                        );
                    })}
                </MarkerClusterGroup>
                <ScaleControl position="bottomright" imperial={false} />
                <ZoomControl position="bottomright" />
            </MapContainer>
        </>
    );
};

MapView.propTypes = {
    markers: PropTypes.oneOfType([PropTypes.any]),
    activeReg: PropTypes.oneOfType([PropTypes.any]),
    mapRef: PropTypes.oneOfType([PropTypes.any]),
    setMapRef: PropTypes.func,
};
MapView.defaultProps = {
    markers: [],
    activeReg: {},
    mapRef: null,
    setMapRef: () => undefined,
};
