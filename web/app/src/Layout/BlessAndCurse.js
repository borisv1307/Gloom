import React, {Component} from "react";
import './BlessAndCurse.css';
class BlessAndCurse extends Component {

    render() {
        return(
            <div className="bless-and-curse">
                <div id="bless" style={{display: 'flex', lineHeight: '40px'}}>
                    <button>+</button>
                    <text>Bless Cards Left: </text>
                    <button>-</button>
                </div>

                <div id="curse" style={{display: 'flex', lineHeight: '40px'}}>
                    <button>+</button>
                    <text>Curse Cards Left: </text>
                    <button>-</button>
                </div>
            </div>
        )
    }
}

export default BlessAndCurse;