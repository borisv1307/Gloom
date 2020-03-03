import './PlayingCards.css'
import React, {Component} from "react";
import Popup from "reactjs-popup";
import BRUTE from '../bruteAbilityCardimages';
import AttackModifier from './AttackModifier.js';

let selectedImages;
selectedImages = [];
let image = [];
let cardsCreated = false;

class PlayingCards extends Component {
	 constructor(props) {
		 super(props);
		 this.state = {
			 cards: [],
		cardsInitial: [],
			 isToggleOn: true
		 }
			this.handleClick = this.handleClick.bind(this);
	 }

	 createCards(){

		if(cardsCreated === false)
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

	 handleClick() {
    this.setState(prevState=> ({
      isToggleOn: !prevState.isToggleOn
    }));
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
	clickCount = 0;
	shuffleClickCount = 0;

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
	        if (task.cardType === "cardsInShortRest") {
	            task.cardType = "cardsInHand";
	        }

	        return task;
	    });

	    this.setState(prevState=> ({
	        ...this.state,
			cards,
			isToggleOn: !prevState.isToggleOn
	    }));

	    if(this.shuffleClickCount === 0){
	    	document.getElementById("reDraw").disabled = true;
		}

	}

	onClickMoveToShortRest(discard) {

	 	this.clickCount = this.clickCount + 1;

    	let cards = this.state.cards.filter((task) => {
    		if (task.cardName === discard.props.children) {
	              task.cardType = "cardsInShortRest";
	         }

	        return task;
	    });

	    this.setState(prevState=> ({
	        ...this.state,
			cards,
			isToggleOn: !prevState.isToggleOn
	    }));

	    if(this.clickCount === 2){
	    	document.getElementById("GetCard").disabled = true;
		}

	}

    render() {

		selectedImages = this.props.abilityCards;

		if(this.props.characterName === 'Brute')
		{
				image = BRUTE;
		}

		this.createCards();

        var cards = {
	      discardPile: [],
	      lostCards: [],
		  cardsInHand: [],
		  cardsInShortRest: []
	    }


		this.state.cards.forEach ((card) => {
			if(card.cardType === "cardsInHand" || card.cardType === "cardsInShortRest") {
				cards[card.cardType].push(
				<div key={card.id}
				  onDragStart = {(event) => this.onDragStart(event, card.cardName)}
				  draggable
				  className="cards-in-hand"
                    style = {{backgroundImage: card.backgroundImage}}>
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
						  <button id="GetCard" onClick={()=>{this.onClickMoveToShortRest(cards.discardPile[Math.floor(Math.random() * cards.discardPile.length)])}}>
						  {this.state.isToggleOn ? 'Get Card' : 'Get New Card'}
					  </button>
					  		{cards.cardsInShortRest}
						  <br/>
						  <br/>
						  <button id="sendToLost" onClick={()=>{this.onClickSendToLost(cards.cardsInShortRest); close();}} >
							  {this.state.isToggleOn ? 'Send to Lost' : 'Continue'}
						  </button>
						  <button id="reDraw" onClick={()=>{this.onClickReDraw(cards.discardPile);}} >
							   Redraw
						  </button>
					  </div>
					</div>
							)}
					</Popup>
					}
			  </div>
	      <div id="top">
                  <div className="discard-pile" style={{flexDirection: "column", textAlign: "top"}}
				    onDragOver={(event)=>this.onDragOver(event)}
                       onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
                      <text>Discard Pile</text>
                      {cards.discardPile}
                  </div>

                  <AttackModifier/>

                  <div className="lost-cards-pile" style={{flexDirection: "column", textAlign: "top" }}
				 onDragOver={(event)=>this.onDragOver(event)}
				 onDrop={(event)=>this.onDrop(event, "lostCards")}>
                      <text>Lost Cards</text>
                      {cards.lostCards}
                  </div>
              </div>

              <div id = "CardsInHand">
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
