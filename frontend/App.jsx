import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { ROUTES, ROUTE_ELEMENT } from 'view/routes';

function App() {
    return (
        <Routes>
            {ROUTES.map((route) => (
                <Route
                    path={route.path}
                    key={route.id}
                    element={ROUTE_ELEMENT[route.name]}
                />
            ))}
        </Routes>
    );
}

export default App;
