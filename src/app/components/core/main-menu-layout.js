import { Nav, NavItem } from 'react-bootstrap';
import { IndexLinkContainer, LinkContainer } from 'react-router-bootstrap';

import { URL, URL_LIST, URL_CALENDAR, URL_CLIENTS, URL_LOGOUT } from "../../constants/config";
import { icon_index } from "../../constants/icons";

export default function MainMenuLayout(props){


    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-md-1">
                    <Nav bsStyle="pills" stacked activeKey={1}>
                        <LinkContainer to="/index/"><NavItem eventKey={0}><span
                            className={icon_index} aria-hidden="true"/></NavItem></LinkContainer>
                        <IndexLinkContainer to={URL_CALENDAR}><NavItem eventKey={1}><span
                            className="glyphicon glyphicon-calendar"
                            aria-hidden="true"/></NavItem></IndexLinkContainer>
                        <LinkContainer to={URL_LIST}><NavItem eventKey={2}><span
                            className="glyphicon glyphicon-list-alt" aria-hidden="true"/></NavItem></LinkContainer>
                        <LinkContainer to={URL_CLIENTS}><NavItem eventKey={3}><span
                            className="glyphicon glyphicon-user" aria-hidden="true"/></NavItem></LinkContainer>
                        <LinkContainer to={URL_LOGOUT}><NavItem eventKey={4}><span
                            className="glyphicon glyphicon-log-out" aria-hidden="true"/></NavItem></LinkContainer>
                    </Nav>

                </div>

                <div className="col-md-11">
                    <main>
                        {props.children}
                    </main>
                </div>
            </div>
        </div>);
}