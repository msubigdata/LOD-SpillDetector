import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { useAxios } from 'hooks/useAxios';

const Login = ({ active, setActive }) => {
    const { response } = useAxios({
        url: '/api/v1/region',
    });

    return (
        <main className="form-signin w-50 d-block mx-auto mt-5">
            <form>
                <h1 className="h3 mb-3 fw-normal text-center">
                    Вход в систему
                </h1>

                <div className="form-floating mb-3">
                    Имя пользователя
                    <input
                        type="email"
                        className="form-control"
                        id="floatingInput"
                        placeholder="name@example.com"
                    />
                </div>
                <div className="form-floating mb-3">
                    Пароль
                    <input
                        type="password"
                        className="form-control"
                        id="floatingPassword"
                        placeholder="Password"
                    />
                </div>
                {response && response.length ? (
                    <select
                        className="form-select mb-3"
                        aria-label="Default select example"
                        onChange={(e) =>
                            setActive(
                                response.find(
                                    (el) =>
                                        el?.id?.toString() === e.target.value
                                )
                            )
                        }
                        value={active && active.id}
                    >
                        {response.map((reg) => (
                            <option value={reg.id} key={reg.id}>
                                {reg.name}
                            </option>
                        ))}
                    </select>
                ) : undefined}
                <Link
                    className="w-100 btn btn-lg btn-danger text-black"
                    type="submit"
                    to="/map"
                >
                    Войти
                </Link>
            </form>
        </main>
    );
};

Login.defaultProps = {
    active: undefined,
    setActive: () => undefined,
};
Login.propTypes = {
    active: PropTypes.oneOfType([PropTypes.any]),
    setActive: PropTypes.func,
};

export default Login;
