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
		this.state = {
		    objectArray: itemList
		};
	}

	resetValues = () =>{
	  // By calling the belowe method will reset the selected values programatically
	  this.multiselectRef.current.resetSelectedValues();
	}

	getSelectedProject = () =>{
	  let selectedProject = this.multiselectRef.getSelectedItems();
	  let i;
	  let Object = [];
	  for(i = 0; i < selectedProject.length; i++){
			Object.push(selectedProject[i].key)
	  }

	  console.log(Object);
	  document.getElementById("items_hidden").value = Object;
	};

	getfilterData =() =>{
		this.getSelectedProject();

	};



    render() {

        return (
            <div  className="Items">
                <div style={{position: "absolute", width: "40%", right:"30%"}}>
               <form onSubmit={this.handleSubmit}>
                   <label>Select Items</label>
                   <br/>
                   <br/><Multiselect
                   options={this.state.objectArray}
                   displayValue="key"
                   ref= {(ref)=>this.multiselectRef=ref}
                   placeholder="Project Name"/>
                   <button type="button" className="btn btn-success" onClick={this.getfilterData}>Finalize Items</button>
               </form>
                    <input type="hidden" name="items_hidden" id="items_hidden" value=""/>
                </div>
            </div>
        )


    }

}

export default ItemSelection;
