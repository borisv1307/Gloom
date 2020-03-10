import './PlayingCards.css'
import React, {Component} from "react";
import Popup from "reactjs-popup";
import BRUTE from '../bruteAbilityCardimages';

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
			 isToggleOn: true,
			 "decks": {
                "discard": {
                    "cards": [],
                    "isHidden": false
                },
                "selected": {
                    "cards": [],
                    "isHidden": false
                },
                "deck": {
                    "cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
                    "isHidden": true
                }
            },
            "onclick": (deck_name) => this.handleClickDeck(deck_name)
		 }
			this.handleClick = this.handleClick.bind(this);
	 }

	 createCards(){

		if(cardsCreated == false)
		{
			for(let i = 0;i<selectedImages.length;i++)
			{
				let currentId = selectedImages[i];

				this.state.cards.push({id: currentId, cardName:image[currentId].cardName, cardType:"cardsInHand", backgroundImage: "url(" + image[currentId].src + ")", imgSrc:image[currentId].src})
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

	    if(this.shuffleClickCount == 0){
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

	    if(this.clickCount == 2){
	    	document.getElementById("GetCard").disabled = true;
		}

	}

	handleClickDeck(deck_name) {
        if (deck_name === "discard") {
            this.reset();
            return;
        }
        this.randomSelect();
    }

    randomSelect() {
        const [deck, discard, selected] = this.getDecks();
        if (deck.length === 0) {
            return;
        }
        const random_idx = this.randomIndex(deck);
        const item = deck[random_idx];
        const new_discard = discard.concat(selected);
        const new_selected = [item];
        const new_deck = this.removeByIndex(deck, random_idx)

        this.setDecks(new_deck, new_discard, new_selected);
    }

    removeByIndex(array, index) {
        return array.filter(function (el, i) {
            return index !== i;
        });
    }

    randomIndex(array) {
        return Math.floor(Math.random() * array.length);
    }

    reset() {
        const [deck, selected, discard] = this.getDecks();
        const new_deck = deck
            .concat(selected)
            .concat(discard);

        this.setDecks(new_deck, [], [])
    }

    getDecks() {
        const decks = this.state.decks;
        return [decks.deck.cards, decks.selected.cards, decks.discard.cards];
    }

    setDecks(deck, discard, selected) {
        this.setState({
            "decks": {
                "deck": {
                    "cards": deck
                },
                "discard": {
                    "cards": discard
                },
                "selected": {
                    "cards": selected
                }
            }
        })
    }

    render() {

		const decks_names = ["discard", "selected"];
        const decks = decks_names.map(
            (key, idx) =>
                <Deck
                    key={idx}
                    name={key}
                    cards={this.state.decks[key].cards}
                    onclick={this.state.onclick}
                />
        );

        var cardsLeft = this.state.decks["deck"].cards.length;

		selectedImages = this.props.abilityCards;

		if(this.props.characterName == 'Brute')
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
                    // style = {{backgroundImage: card.backgroundImage}}
				>
					<img src={card.imgSrc}/>
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

					<Popup trigger={<button disabled={cards.discardPile.length < 2} id="shortrestbutton" onClick={() => {
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
                  <div id="discard-pile" className="discard-pile" style={{flexDirection: "column", textAlign: "top"}}
				    onDragOver={(event)=>this.onDragOver(event)}
                       onDrop={(event)=>{this.onDrop(event, "discardPile")}}>
                      <text>Discard Pile</text>
                      {cards.discardPile}
                  </div>
                  <div className="attack-modifier" style={{flexDirection: "row"}}>
                    {decks}
                    <text>Cards Left: {cardsLeft}</text>
                    <button onClick={() => this.randomSelect()}>Pull Card</button>
                    <button onClick={() => this.reset()}>Reset</button>
                  </div>

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

class Deck extends Component {
    get_cards() {
        if (this.props.hidden) {
            return this.props.cards.map(
                (val, idx) =>
                    <Card key={idx}/>
            );
        }
        return this.props.cards.map(
            (val, idx) =>
                <Card key={idx} value={val}/>
        );
    }

    render() {
        let cards = this.get_cards();

        return (
            <div style={{justifyContent:"flex-start"}}
                 className="attack-deck" onClick={() => this.props.onclick(this.props.name)}>
                <div>{this.props.name}</div>
                <div style={{display:"flex",flexDirection: "row", flexWrap:"wrap"}}>{cards}</div>
            </div>
        )
    }
}

function Card(props) {
    return (
        <div className="attack-card" style={{flexDirection: "row", textAlign: "top"}}>
            {props.value}</div>
    )
}

export default PlayingCards;
