import { Link, browserHistory } from 'react-router';
import { Button } from 'react-bootstrap';

function closeModal(){
        browserHistory.push('/mybookings/');
    }

function ModalDialog(props) {

    let modal_header = "";
    if (props.title != undefined) {
        modal_header = <div className="modal-header">
            <button type="button" className="close" data-dismiss="modal" aria-label="Close" onClick={closeModal}>
                <span aria-hidden="true">&times;</span></button>
            <h4 className="modal-title" id="mySmallModalLabel">{props.title}</h4>
        </div>
    }
    let modal_body = "";
    if (props.body != undefined) {
        modal_body = <div className="modal-body">
            {props.body}
        </div>
    }
    let modal_footer = "";
    if (props.buttons != undefined) {
        modal_footer = <div className="modal-footer">
            {props.buttons}
        </div>
    }


    return (
        <div className={"modal " + props.className + "" + props.id} role="dialog"
             aria-labelledby="mySmallModalLabel">
            <div className={"modal-dialog "+ props.size} role="document">
                <div className="modal-content">
                    {modal_header}
                    {modal_body}
                    {modal_footer}
                </div>
            </div>
        </div>
    );
}

export default ModalDialog;