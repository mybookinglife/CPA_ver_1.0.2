import { icon_login } from '../../constants/icons';
import { Link } from 'react-router';
import { URL_LIST } from '../../constants/config';

export default function CommonLayout(props){
    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-md-10">
                    <p>My booking !!!</p>
                </div>
                <div className="col-md-2">
                    <Link to={URL_LIST}><span
                    className={icon_login}/> Private account</Link>
                </div>
            </div>
            <div className="row">
                <img src="/static/img/logo2.png"/>
            </div>
        </div>);
}