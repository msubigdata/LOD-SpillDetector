import React from 'react';
import PropTypes from 'prop-types';
import DtPicker from 'react-calendar-datetime-picker';
import './styles/main.scss';

export const DateRangePicker = ({ onChange }) => {
    return (
        <div className="picker_wrapper">
            <DtPicker
                onChange={onChange}
                type="range"
                fromLabel="От"
                toLabel="До"
                headerClass="picker_header"
                placeholder="Выберите дату"
            />
        </div>
    );
};

DateRangePicker.propTypes = {
    onChange: PropTypes.func.isRequired,
};
