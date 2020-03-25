import React from 'react';
import './items.css';


class Items extends React.Component {
    render() {
        return (
            <div id="itemsBox">
                <p>Items List</p>
                <p>{this.props.items}</p>


            </div>
        );
    }
}

export default Items;
