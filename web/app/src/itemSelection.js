import React, {Component} from 'react';
import './itemSelection.css'
import itemList from './itemsList.js';
import { Multiselect } from 'multiselect-react-dropdown';
import ReactDOM from "react-dom";
import App from "./App";
import Items from "./items";

class ItemSelection extends Component {
    constructor(props) {
        super(props);
        this.multiselectRef = React.createRef();
        this.state = {
            items: itemList

        }
    }

    onSelect(selectedList, selectedItem) {

    }

    onRemove(selectedList, removedItem) {

    }

    handleSubmit = (event) => {
        event.preventDefault();
        this.multiselectRef.current.getSelectedItems();
        console.log(this.multiselectRef.current.getSelectedItems());

    }



    render() {

        return (
            <div style={{position: "absolute", width: "40%", right:"30%"}}>
               <form onSubmit={this.handleSubmit}>
                   <label>Select Items</label>
                   <br/>
                   <br/>
               <Multiselect
                options={this.state.items}
                ref={this.multiselectRef}
                selectedItem={this.state.selectedItem}
                onSelect={this.onSelect}
                onRemove={this.onRemove}
                displayValue="name"
                />
                <input type="submit" />
                </form>
            </div>
        )


    }

}
function goToItems(props) {

    ReactDOM.render(<Items items={this.multiselectRef.current.getSelectedItems()} />, document.getElementById('root'));

}

export default ItemSelection;
