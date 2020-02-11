import React, {Component} from "react";
import './ShortRest.css'
import Popup from "reactjs-popup";

export default class ShortRest extends Component {
    constructor(props) {
        super(props);
        this.state = {
            taskName: this.props.taskName,
            discardPile: this.props.discardPile
        };
    }
        render()
        {

            return (
                <div className="shortrest-container">
                    <Popup trigger={<button className="button" onClick={() => {
                    }}> Short Rest </button>} modal>
                        {close => (
                            <div className="modal">
                                <a className="close" onClick={close}>
                                    &times;
                                </a>
                                <div className="header"> Send to lost or Reshuffle?</div>
                                <div className="card-container">
                                    discard card names: {this.props.taskName} {this.props.discardPile}
                                    <br/>
                                    <br/>
                                </div>
                                <div className="actions">
                                    <button
                                        className="button"
                                        onClick={() => {
                                            console.log("reshuffle ");
                                        }}
                                    >
                                        Reshuffle
                                    </button>
                                    <button
                                        className="button"
                                        onClick={() => {
                                            console.log("sent to lost ");
                                            close();
                                        }}
                                    >
                                        Send to Lost
                                    </button>
                                </div>
                            </div>
                        )}
                    </Popup>
                </div>
            );
        }
}
