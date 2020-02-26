import './PlayingCards.css'
import React, {Component} from "react";
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
		cardsInitial: [],
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
            "onclick": (deck_name) => this.handleClick(deck_name)
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

	handleClick(deck_name) {
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
	      <div id="top">
                  <div className="discard-pile" style={{flexDirection: "column", textAlign: "top"}}
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