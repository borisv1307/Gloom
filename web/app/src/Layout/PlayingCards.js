import './PlayingCards.css'
import React, {Component} from "react";

class PlayingCards extends Component {
    state = {
	tasks: [
      {id: "1", taskName:"Trample 1",type:"cardsInHand", backgroundImage: "red"},
      {id: "2", taskName:"Trample 2", type:"cardsInHand", backgroundImage:"blue"},
      {id: "3", taskName:"Trample 3", type:"cardsInHand", backgroundImage:"green"},
      {id: "4", taskName:"Trample 4", type:"cardsInHand", backgroundImage:"yellow"},
	  {id: "5", taskName:"Trample 5", type:"cardsInHand", backgroundImage:"red"},
      {id: "6", taskName:"Trample 6", type:"cardsInHand", backgroundImage:"blue"},
	  {id: "7", taskName:"Trample 7",type:"cardsInHand", backgroundImage: "green"},
      {id: "8", taskName:"Trample 8", type:"cardsInHand", backgroundImage:"yellow"},
      {id: "9", taskName:"Trample 9", type:"cardsInHand", backgroundImage:"red"},
      {id: "10", taskName:"Trample 10", type:"cardsInHand", backgroundImage:"blue"},
	  {id: "11", taskName:"Trample 11", type:"cardsInHand", backgroundImage:"green"},
      {id: "12", taskName:"Trample 12", type:"cardsInHand", backgroundImage:"yellow"}

	]
    }

    onDragStart = (event, taskName) => {
    	console.log('dragstart on div: ', taskName);
    	event.dataTransfer.setData("taskName", taskName);
	}
	onDragOver = (event) => {
	    event.preventDefault();
	}

	onDrop = (event, cat) => {
	    let taskName = event.dataTransfer.getData("taskName");

	    let tasks = this.state.tasks.filter((task) => {
	        if (task.taskName == taskName) {
	            task.type = cat;
	        }
	        return task;
	    });

	    this.setState({
	        ...this.state,
	        tasks
	    });
	}

    render() {
        var tasks = {
	      discardPile: [],
	      lostCards: [],
		  cardsInHand: []
	    }

		this.state.tasks.forEach ((task) => {
		  tasks[task.type].push(
		    <div key={task.id}
		      onDragStart = {(event) => this.onDragStart(event, task.taskName)}
		      draggable
		      className="cards"
		      style = {{backgroundColor: task.backgroundImage}}>
		      {task.taskName}
		    </div>
		  );
		});

	    return (
	      <div className="drag-container">
		    <div className="discard-pile" style={{display:"flex", justifyContent:"space-evenly"}}
	    		onDragOver={(event)=>this.onDragOver(event)}
      			onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
	          <span className="group-header">Discard Pile</span>
	          {tasks.discardPile}
	        </div>
	        <div className="lost-cards" style={{display:"flex", justifyContent:"space-evenly"}}
				 onDragOver={(event)=>this.onDragOver(event)}
				 onDrop={(event)=>this.onDrop(event, "lostCards")}>
	          <span className="group-header">Lost Cards</span>
	          {tasks.lostCards}
	        </div>

            <div className="discard-pile" style={{display:"flex", justifyContent:"space-evenly"}}
				onDragOver={(event)=>this.onDragOver(event)}
				onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
				<span className="group-header">Discard Pile</span>
				{tasks.discardPile}
			</div>

			<div className="cards-in-hand" style={{display:"flex", justifyContent:"space-evenly", position: "absolute", bottom: 0}}
				onDragOver={(event)=>this.onDragOver(event)}
				onDrop={(event)=>{this.onDrop(event, "cardsInHand")}}>
				<span className="group-header">Cards In Hand</span>
				{tasks.cardsInHand}
			</div>
	      </div>
	    );
    }
}

export default PlayingCards;