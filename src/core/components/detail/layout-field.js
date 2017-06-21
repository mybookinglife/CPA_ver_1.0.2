import React, { Component } from 'react';
// import LinkedStateMixin from 'react-addons-linked-state-mixin';
import { Form, FormGroup, InputGroup, FormControl, ControlLabel } from 'react-bootstrap';
import DatePicker from 'react-bootstrap-date-picker';
import TimePicker from 'react-bootstrap-time-picker';
// import ReactMixin from 'react-mixin';

class LayoutField extends Component{

    constructor(props) {
        super(props);
        this.state = {
            date_time: this.props.obj.date_time,
            date: this.props.obj.date,
            time: this.props.obj.time,
            company: this.props.obj.company,
            client: this.props.obj.client,
            service: this.props.obj.service,
            expert: this.props.obj.expert,
            note: this.props.obj.note,
            comment: this.props.obj.comment,
            is_new: this.props.obj.is_new,
            is_cansel: this.props.obj.is_cansel,
            is_finished: this.props.obj.is_finished
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeDate = this.handleChangeDate.bind(this);
        this.handleChangeTime = this.handleChangeTime.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
    }

    componentDidMount() {

    }

    handleChange(event){
        this.setState({[event.target.id]: event.target.value});
        this.props.obj[event.target.id] = event.target.value;
    }

    handleChangeDate(value) {
        //debugger;
        let date = value.split('T')[0];

        this.setState({date: date});
        this.props.obj.date = date;
        this.setState({date_time: date + "T" + this.state.time + "Z"});
        this.props.obj.date_time = date + "T" + this.state.time + "Z";

    }


    handleChangeTime(value) {

        let today = new Date(0,0,0,0,0,value)

        var hh = today.getHours();
        if (hh < 10) hh = '0' + hh;
        var mm = today.getMinutes();
        if (mm < 10) mm = '0' + mm;
        var ss = today.getSeconds();
        if (ss < 10) ss = '0' + ss;

        let time =  hh + ':' + mm + ':' + ss;

        this.setState({time: time});
        this.props.obj.time = time;
        this.setState({date_time: this.state.date + "T" + time + "Z"});
        this.props.obj.date_time = this.state.date + "T" + time + "Z";
    }

    handleSelect(event) {
        //debugger;
        this.setState({[event.target.id]: Number(event.target.value)});
        this.props.obj[event.target.id] = Number(event.target.value);
    }

    render(){

        let now = new Date();
        let curMonth = now.getMonth() + 1;
        curMonth = curMonth < 10 ? "0" + curMonth : curMonth;

        // debugger;
        return (<form>
            <Form componentClass="fieldset" inline>
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon>Date</InputGroup.Addon>
                        <DatePicker dateFormat="YYYY-MM-DD" onChange={this.handleChangeDate} value={this.state.date} />
                    </InputGroup>
                </FormGroup>
                {' '}
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon>Time</InputGroup.Addon>
                        <TimePicker start="10:00" end="19:00" format={24} step={15} onChange={this.handleChangeTime} value={this.state.time}/>
                    </InputGroup>
                </FormGroup>
            </Form>

            <Form componentClass="fieldset">
                <FormGroup></FormGroup>
                {' '}
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon>Клиент</InputGroup.Addon>
                        <FormControl id="client" componentClass="select" value={this.state.client} onChange={this.handleSelect}>
                            <option value={1}>Клиент №1</option>
                            <option value={3}>Клиент №2</option>
                            <option value={4}>Клиент №3</option>
                        </FormControl>
                    </InputGroup>
                </FormGroup>
                {' '}
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon>Услуга</InputGroup.Addon>
                        {/*<FormControl id="service" type="text" value={this.state.service} onChange={this.handleChange}/>*/}
                        <FormControl id="service" componentClass="select" value={this.state.service}
                                     onChange={this.handleSelect}>
                            <option value={1}>Мужская стрижка</option>
                            <option value={2}>Женская стрижка</option>
                        </FormControl>
                    </InputGroup>
                </FormGroup>
                {' '}
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon>Специалист</InputGroup.Addon>
                        {/*<FormControl id="expert" type="text" value={this.state.expert} onChange={this.handleChange}/>*/}
                        <FormControl id="expert" componentClass="select" value={this.state.expert}
                                     onChange={this.handleSelect}>
                            <option value={1}>Специалист 2</option>
                            <option value={2}>Специалист 1</option>
                        </FormControl>
                    </InputGroup>
                </FormGroup>
                {' '}
                <FormGroup>
                    <ControlLabel>Примечания клиента</ControlLabel>
                    <FormControl componentClass="textarea" value={this.state.note} readOnly/>
                </FormGroup>
                {' '}
               <FormGroup>
                    <ControlLabel>Комментарий</ControlLabel>
                    <FormControl id="comment" componentClass="textarea" value={this.state.comment} onChange={this.handleChange}/>
                </FormGroup>
           </Form>
        </form>);
    }

}

// ReactMixin(LayoutField.prototype, LinkedStateMixin);

export default LayoutField;
