import axios from 'axios';
import { useState, useEffect } from 'react';

export const useAxios = (
    axiosParams = {
        url: '',
        method: 'GET',
        headers: undefined,
        params: undefined,
        body: undefined,
    }
) => {
    const [response, setResponse] = useState(undefined);
    const [hasError, setHasError] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [shouldRedirect, setShouldRedirect] = useState(false);

    let retries = 0;
    let success = false;
    const maxRetries = 3;

    const fetchData = async (params) => {
        while (retries < maxRetries && !success) {
            try {
                // eslint-disable-next-line no-await-in-loop
                const result = await axios.request(params);
                setResponse(result.data);
                setIsLoading(false);
                success = true;
            } catch (error) {
                if (!axios.isCancel(error)) {
                    setHasError(true);
                    setIsLoading(false);
                    if (error?.response?.status === 404) {
                        setShouldRedirect(true);
                        success = true;
                    }
                } else {
                    success = true;
                }
            }
            retries += 1;
        }
    };

    useEffect(() => {
        setIsLoading(true);
        setResponse(undefined);
        setShouldRedirect(false);
        const source = axios.CancelToken.source();
        if (axiosParams.url && axiosParams.url !== '') {
            fetchData({ ...axiosParams, cancelToken: source.token });
        }
        return () => {
            source.cancel('Cancelling in cleanup');
        };
    }, [axiosParams.params, axiosParams.url]);

    return { response, hasError, isLoading, shouldRedirect };
};
