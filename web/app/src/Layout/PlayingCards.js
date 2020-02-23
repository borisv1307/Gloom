import './PlayingCards.css'
import React, {Component} from "react";
import backOfCard from './backofcard.PNG';
import card from './card1.png';
import BRUTE from '../bruteAbilityCardimages'


let selectedImages;
selectedImages = [];
let image = [];
let cardsCreated = false;


class PlayingCards extends Component {

	createCards(){

		if(cardsCreated == false)
		{
			for(let i = 0;i<selectedImages.length;i++)
			{
				let currentId = selectedImages[i];

				this.state.cards.push({id: currentId, cardName:image[currentId].cardName, cardType:"cardsInHand", backgroundImage: "url(" + image[currentId].src + ")"})
				this.state.cardsInitial.push({id: currentId, cardName:image[currentId].cardName, cardType:"cardsInHand", backgroundImage: "url(" + image[currentId].src + ")"})
			}
			cardsCreated = true;
		}
	}

    state = {
		cards: [],
		cardsInitial: []
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


    render() {

		selectedImages = this.props.abilityCards;

		if(this.props.characterName == 'Brute')
		{
				image = BRUTE;
		}

		this.createCards();

        var cards = {
	      discardPile: [],
	      lostCards: [],
		  cardsInHand: []
	    }


		this.state.cards.forEach ((card) => {
			if(card.cardType === "cardsInHand") {
				cards[card.cardType].push(
				<div key={card.id}
				  onDragStart = {(event) => this.onDragStart(event, card.cardName)}
				  draggable
				  className="cards-in-hand"
                    style = {{backgroundImage: card.backgroundImage}}>
				  {/*{card.cardName}*/}
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
	    );
    }
}

export default PlayingCards;