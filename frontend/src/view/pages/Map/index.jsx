import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { MapView } from 'view/components/MapView';
import test from 'assets/icons/marker-alert.svg';
import marker from './markers-2017.json';
import './styles/main.scss';

const Map = ({ active }) => {
    const [drawerIsOpen, setDrawerIsOpen] = useState(false);
    const [markers, setMarkers] = useState(marker);

    useEffect(() => {
        setMarkers(marker);
    }, [marker]);

    const [mapRef, setMapRef] = useState(null);

    const zoomIn = (area) => {
        mapRef.setView(
            [
                (area[0][1][0] + area[0][0][0]) / 2,
                (area[0][1][1] + area[0][0][1]) / 2,
            ],
            14
        );
    };

    useEffect(() => {
        if (mapRef) {
            setTimeout(() => {
                mapRef.invalidateSize();
            }, [500]);
        }
    }, [drawerIsOpen, mapRef]);

    return (
        <main className="main_wrapper">
            <MapView
                markers={markers}
                activeReg={active}
                setMapRef={setMapRef}
                mapRef={mapRef}
            />
            <div className={`sidebar ${drawerIsOpen && 'isOpen'}`}>
                <button
                    type="button"
                    className="drawer_btn"
                    onClick={() => {
                        setDrawerIsOpen(!drawerIsOpen);
                    }}
                >
                    <img src={test} alt="mark" />
                </button>
                <div className="button_wrapper">
                    {markers.map((m, i) => {
                        const freshImg = m?.images[0];
                        return (
                            <button
                                type="button"
                                className="marker_button"
                                key={`${i + 1}`}
                                onClick={() => zoomIn(m.area)}
                            >
                                <img
                                    src={freshImg.url}
                                    alt={freshImg.url}
                                    style={{ borderColor: m.color }}
                                    className="marker_img"
                                />
                                <div className="text_wrapper">
                                    <span>Сильный уровень загрязнения,</span>
                                    <span>More Info</span>
                                    <span>More Test Info</span>
                                </div>
                            </button>
                        );
                    })}
                </div>
            </div>
        </main>
    );
};

Map.propTypes = {
    active: PropTypes.oneOfType([PropTypes.any]),
};
Map.defaultProps = {
    active: {},
};

export default Map;
