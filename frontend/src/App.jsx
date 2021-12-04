import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import { ROUTES } from 'view/routes';
import { Map } from 'view/pages';
import Login from 'view/pages/Login';

function App() {
    const [activeRegion, setActiveRegion] = useState();
    return (
        <Routes>
            {ROUTES.map((route) => (
                <Route
                    path={route.path}
                    key={route.id}
                    element={
                        route.name === 'map' ? (
                            <Map active={activeRegion} />
                        ) : (
                            <Login
                                setActive={setActiveRegion}
                                active={activeRegion}
                            />
                        )
                    }
                />
            ))}
        </Routes>
    );
}

export default App;
