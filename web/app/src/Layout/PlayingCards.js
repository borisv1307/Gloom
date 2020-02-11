import './PlayingCards.css'
import React, {Component} from "react";

class PlayingCards extends Component {
    state = {
	cards: [
      {id: "1", cardName:"Trample 1",cardType:"cardsInHand", backgroundImage: "red"},
      {id: "2", cardName:"Trample 2", cardType:"cardsInHand", backgroundImage:"blue"},
      {id: "3", cardName:"Trample 3", cardType:"cardsInHand", backgroundImage:"green"},
      {id: "4", cardName:"Trample 4", cardType:"cardsInHand", backgroundImage:"yellow"},
	  {id: "5", cardName:"Trample 5", cardType:"cardsInHand", backgroundImage:"red"},
      {id: "6", cardName:"Trample 6", cardType:"cardsInHand", backgroundImage:"blue"},
	  {id: "7", cardName:"Trample 7",cardType:"cardsInHand", backgroundImage: "green"},
      {id: "8", cardName:"Trample 8", cardType:"cardsInHand", backgroundImage:"yellow"},
      {id: "9", cardName:"Trample 9", cardType:"cardsInHand", backgroundImage:"red"},
      {id: "10", cardName:"Trample 10", cardType:"cardsInHand", backgroundImage:"blue"},
	  {id: "11", cardName:"Trample 11", cardType:"cardsInHand", backgroundImage:"green"},
      {id: "12", cardName:"Trample 12", cardType:"cardsInHand", backgroundImage:"yellow"}

	]
    }

    onDragStart = (event, cardName) => {
    	console.log('dragstart on div: ', cardName);
    	event.dataTransfer.setData("cardName", cardName);
	}
	onDragOver = (event) => {
	    event.preventDefault();
	}

	onDrop = (event, changeCardType) => {
	    let cardName = event.dataTransfer.getData("cardName");

	    let cards = this.state.cards.filter((task) => {
	        if (task.cardName == cardName) {
	            task.cardType = changeCardType;
	        }
	        return task;
	    });

	    this.setState({
	        ...this.state,
	        cards
	    });
	}

    render() {
        var cards = {
	      discardPile: [],
	      lostCards: [],
		  cardsInHand: []
	    }

		this.state.cards.forEach ((task) => {
		  cards[task.cardType].push(
		    <div key={task.id}
		      onDragStart = {(event) => this.onDragStart(event, task.cardName)}
		      draggable
		      className="cards"
		      style = {{backgroundColor: task.backgroundImage}}>
		      {task.cardName}
		    </div>
		  );
		});

	    return (
	      <div className="drag-container">
		    <div className="discard-pile" style={{display:"flex", justifyContent:"space-evenly"}}
	    		onDragOver={(event)=>this.onDragOver(event)}
      			onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
	          <span className="group-header">Discard Pile</span>
	          {cards.discardPile}
	        </div>
	        <div className="lost-cards" style={{display:"flex", justifyContent:"space-evenly"}}
				 onDragOver={(event)=>this.onDragOver(event)}
				 onDrop={(event)=>this.onDrop(event, "lostCards")}>
	          <span className="group-header">Lost Cards</span>
	          {cards.lostCards}
	        </div>

            <div className="discard-pile" style={{display:"flex", justifyContent:"space-evenly"}}
				onDragOver={(event)=>this.onDragOver(event)}
				onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
				<span className="group-header">Discard Pile</span>
				{cards.discardPile}
			</div>

			<div className="cards-in-hand" style={{display:"flex", justifyContent:"space-evenly", position: "absolute", bottom: 0}}
				onDragOver={(event)=>this.onDragOver(event)}
				onDrop={(event)=>{this.onDrop(event, "cardsInHand")}}>
				<span className="group-header">Cards In Hand</span>
				{cards.cardsInHand}
			</div>
	      </div>
	    );
    }
}

export default PlayingCards;