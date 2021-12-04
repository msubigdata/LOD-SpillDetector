// eslint-disable-next-line import/no-extraneous-dependencies
const createProxyMiddleware = require('http-proxy-middleware');

const DEFAULT_BACKEND_PORT = 8000;
const DEFAULT_BACKEND_HOST = '0.0.0.0';
const DEFAULT_PROTOCOL = 'http';

const INTERNAL_API = process.env.REACT_APP_FRONTEND_API_URL;

const BACKEND_PORT_ENV = process.env.REACT_APP_BACKEND_PORT;

const IS_DOCKER = !!BACKEND_PORT_ENV;
const BACKEND_PORT = IS_DOCKER ? BACKEND_PORT_ENV : DEFAULT_BACKEND_PORT;
const BACKEND_HOST = IS_DOCKER ? 'backend' : DEFAULT_BACKEND_HOST;

// eslint-disable-next-line func-names
module.exports = function (app) {
    app.use(
        createProxyMiddleware('/api', {
            target: `${
                INTERNAL_API ||
                `${DEFAULT_PROTOCOL}://${BACKEND_HOST}:${BACKEND_PORT}`
            }`,
            changeOrigin: true,
        })
    );
};
