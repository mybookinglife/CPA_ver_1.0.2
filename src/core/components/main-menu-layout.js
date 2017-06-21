import { Nav, NavItem } from 'react-bootstrap';
import { IndexLinkContainer, LinkContainer } from 'react-router-bootstrap';

export default function MainMenuLayout(props){


    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-md-1">
                    <Nav bsStyle="pills" stacked activeKey={1}>
                        <IndexLinkContainer to="/"><NavItem eventKey={1}><span className="glyphicon glyphicon-calendar"
                                                                               aria-hidden="true"/></NavItem></IndexLinkContainer>
                        <LinkContainer to="/mybookings/"><NavItem eventKey={2}><span
                            className="glyphicon glyphicon-list-alt" aria-hidden="true"/></NavItem></LinkContainer>
                        <LinkContainer to="/myclients/"><NavItem eventKey={3}><span className="glyphicon glyphicon-user"
                                                                                    aria-hidden="true"/></NavItem></LinkContainer>
                        <LinkContainer to="/logout/"><NavItem eventKey={3}><span className="glyphicon glyphicon-log-out"
                                                                                 aria-hidden="true"/></NavItem></LinkContainer>
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