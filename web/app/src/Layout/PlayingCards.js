import './PlayingCards.css'
import React, {Component} from "react";
import card from './card1.png';
import Popup from "reactjs-popup";

class PlayingCards extends Component {
    state = {
	cards: [
      {id: "1", cardName:"Trample 1", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "2", cardName:"Trample 2", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "3", cardName:"Trample 3", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "4", cardName:"Trample 4", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
	  {id: "5", cardName:"Trample 5", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "6", cardName:"Trample 6", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
	  {id: "7", cardName:"Trample 7", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "8", cardName:"Trample 8", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
      {id: "9", cardName:"Trample 9", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
      {id: "10", cardName:"Trample 10", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
	  {id: "11", cardName:"Trample 11", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
      {id: "12", cardName:"Trample 12", cardType:"discardPile", backgroundImage: "url(" + card + ")"}

	],
		cardsInitial: [
      {id: "1", cardName:"Trample 1", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "2", cardName:"Trample 2", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "3", cardName:"Trample 3", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "4", cardName:"Trample 4", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
	  {id: "5", cardName:"Trample 5", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "6", cardName:"Trample 6", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
	  {id: "7", cardName:"Trample 7", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "8", cardName:"Trample 8", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "9", cardName:"Trample 9", cardType:"cardsInHand", backgroundImage: "url(" + card + ")"},
      {id: "10", cardName:"Trample 10", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
	  {id: "11", cardName:"Trample 11", cardType:"discardPile", backgroundImage: "url(" + card + ")"},
      {id: "12", cardName:"Trample 12", cardType:"discardPile", backgroundImage: "url(" + card + ")"}
	],
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
	        if (task.cardName === cardName) {
	            task.cardType = changeCardType;

	            if(task.cardType === "cardsInHand") {
	            	for(let i=0; i<this.state.cards.length; i++){
	            		if(task.cardName === this.state.cards[i].cardName){
	            			task.backgroundImage = this.state.cardsInitial[i].backgroundImage;
						}
					}
				}
	        }
	        return task;
	    });

	    this.setState({
	        ...this.state,
			cards
	    });
	}

	onClickSendToLost() {

    	let cards = this.state.cards.filter((task) => {
	        if (task.cardType === "cardsInShortRest") {
	            task.cardType = "lostCards";
	        }
	        else if (task.cardType === "discardPile") {
	        	task.cardType = "cardsInHand";
			}
	        return task;
	    });

	    this.setState({
	        ...this.state,
			cards
	    });
	}

	onClickReDraw(discard) {

    	let cards = this.state.cards.filter((task) => {
	        if (task.cardName === discard[discard.length-1].props.children) {
	            task.cardType = "discardPile";
	        }
	        return task;
	    });

	    this.setState({
	        ...this.state,
			cards
	    });
	}

	onClickMoveToShortRest(discard) {

    	let cards = this.state.cards.filter((task) => {
	        if (task.cardName === discard[Math.floor(Math.random() * discard.length)].props.children) {
	            task.cardType = "cardsInShortRest";
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
		  cardsInHand: [],
		  cardsInShortRest: []
	    }


		this.state.cards.forEach ((card) => {
			if(card.cardType === "cardsInHand") {
				cards[card.cardType].push(
				<div key={card.id}
				  onDragStart = {(event) => this.onDragStart(event, card.cardName)}
				  draggable
				  className="cards-in-hand"
                    style = {{backgroundImage: card.backgroundImage}}>
				  {card.cardName}
				</div>
			  );
			}
			else{
				cards[card.cardType].push(
				<div key={card.id}
				  onDragStart = {(event) => this.onDragStart(event, card.cardName)}
				  draggable
				  className="cards"
				  style = {{backgroundImage: card.backgroundImage}}>
				  {card.cardName}
				</div>
			  );
			}

		});

	    return (
			<div>
				<div className="shortrest">
				  {
					cards.discardPile.length > 1 &&
					<Popup trigger={<button className="shortrest" onClick={() => {
					 }}> Short Rest </button>} modal>
					{close => (
				  <div className="modal">
					  <a className="close" onClick={close}>
						  &times;
					  </a>
					  <div className="header"> Send to lost or Redraw</div>
					  <div className="card-container" >
						  <button onClick={()=>{this.onClickMoveToShortRest(cards.discardPile)}}>
						  Get Card
					  </button>
					  {cards.cardsInShortRest}
						  <br/>
						  <br/>
						  <button id="sendToLost" onClick={()=>{this.onClickSendToLost(cards.cardsInShortRest); close();}} >
							  Send to Lost
						  </button>
						  <button id="reDraw" onClick={()=>{this.onClickReDraw(cards.cardsInShortRest);}} >
							  Redraw
						  </button>
					  </div>
					</div>
							)}
					</Popup>
					}
			  </div>
	      <div className="drag-container">
		    <div className="discard-pile" style={{display:"flex", flexDirection: "column", textAlign: "top"}}
	    		onDragOver={(event)=>this.onDragOver(event)}
      			onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
				<text>Discard Pile</text>
	          {cards.discardPile}
	        </div>
	        <div className="lost-cards-pile" style={{display:"flex", flexDirection: "column", textAlign: "top" }}
				 onDragOver={(event)=>this.onDragOver(event)}
				 onDrop={(event)=>this.onDrop(event, "lostCards")}>
				<text>Lost Cards</text>
	          {cards.lostCards}
	        </div>

            <div className="discard-pile" style={{display:"flex", flexDirection: "column", textAlign: "top"}}
				onDragOver={(event)=>this.onDragOver(event)}
				onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
				<text>Discard Pile</text>
				{cards.discardPile}
			</div>

			<div className="cards-in-hand-pile" style={{display:"flex", justifyContent:"space-evenly", position: "absolute", bottom: 0}}
				 onDragOver={(event)=>this.onDragOver(event)}
				 onDrop={(event)=>{this.onDrop(event, "cardsInHand")}}>
				<text>Cards In Hand</text>
				{cards.cardsInHand}
			</div>
	      </div>
			</div>
	    );
    }
}

export default PlayingCards;
