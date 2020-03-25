import React, {Component} from "react";
import './AttackModifier.css';
import AttackModifierDeck from '../Perks/AttackModifierDeck.json'

let blessDiscard = 0;
let curseDiscard = 0;

const cardName = AttackModifierDeck;

class AttackModifier extends Component {
    constructor(props) {
        super(props);
        this.state = {
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
                    "cards": this.props.cards,
                    "isHidden": true
                },
                "init_deck": {
                    "cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
                    "isHidden": true
                },
            },
            bless: 10,
            curse: 10
        }
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
        const new_deck = this.removeByIndex(deck, random_idx);

        if (item === "2xB") {
            blessDiscard += 1;
        }

        if (item === "0C") {
            curseDiscard += 1;
        }

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

    resetBlessAndCurse() {

        let currentBless = this.state.bless;
        this.setState({
            bless: currentBless + blessDiscard
        });

        blessDiscard = 0;

        let currentCurse = this.state.curse;
        this.setState({
            curse: currentCurse + curseDiscard
        });
        curseDiscard = 0;

    }

    resetAttackDecks() {
        const [deck, selected, discard] = this.getDecks();
        let new_deck;

        let discardLength = discard.length;
        let selectedLength = selected.length;

        for (var i = 0; i <= selectedLength; i++) {
            if (selected[i] === "2xB") {
                selected.splice(i, 1);
            } else if (selected[i] === "0C") {
                selected.splice(i, 1);
            }
        }

        for (i = 0; i < discardLength; i++) {
            if (discard[i] === "2xB") {
                discard.splice(i, 1);
                i--;
            }
            if (discard[i] === "0C") {
                discard.splice(i, 1);
                i--;
            }
        }

        new_deck = deck.concat(selected).concat(discard);

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

    onClickBlessPlus() {
        if (this.state.bless >= 0 && this.state.bless <= 10) {
            let currentBless = this.state.bless;
            this.setState({
                bless: currentBless - 1
            });
            this.state.decks["deck"].cards.push("2xB");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);

        }
    }

    onClickBlessMinus() {
        if (this.state.bless >= 0 && this.state.bless <= 10) {
            for (let i = 0; i < this.state.decks["deck"].cards.length; i++) {
                if (this.state.decks["deck"].cards[i] === "2xB") {
                    this.state.decks["deck"].cards.splice(i, 1);
                    let currentBless = this.state.bless;
                    this.setState({
                        bless: currentBless + 1
                    });
                    this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
                    return;
                }
            }
        }
    }

    onClickCursePlus() {
        if (this.state.curse >= 0 && this.state.curse <= 10) {
            let currentCurse = this.state.curse;
            this.setState({
                curse: currentCurse - 1
            });
            this.state.decks["deck"].cards.push("0C");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);

        }
    }

    onClickCurseMinus() {
        if (this.state.curse >= 0 && this.state.curse <= 10) {
            for (let i = 0; i < this.state.decks["deck"].cards.length; i++) {
                if (this.state.decks["deck"].cards[i] === "0C") {
                    this.state.decks["deck"].cards.splice(i, 1);
                    let currentCurse = this.state.curse;
                    this.setState({
                        curse: currentCurse + 1
                    });
                    this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
                    return;
                }
            }
        }
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

        let cardsLeft = this.state.decks["deck"].cards.length;
        let blessLeft = this.state.bless;
        let curseLeft = this.state.curse;
        return (
            <div>
                <div className="attack-modifier" style={{flexDirection: "row"}}>
                    {decks}
                    <text className="text-cards-left">Cards Left: {cardsLeft}</text>
                    <button className="button-pull-card" disabled={cardsLeft <= 0}
                            onClick={() => this.randomSelect()}>Pull Card
                    </button>
                    <button className="button-shuffle" onClick={() => {
                        this.resetAttackDecks();
                        this.resetBlessAndCurse();
                    }}>Shuffle
                    </button>
                </div>

                <div className="bless-and-curse">
                    <div id="bless" style={{display: 'flex', lineHeight: '40px'}}>
                        <button className="button-plus-minus" disabled={blessLeft <= 0}
                                onClick={() => this.onClickBlessPlus()}>+
                        </button>
                        <text>Bless Cards Left: {blessLeft}</text>
                        <button className="button-plus-minus" disabled={blessLeft >= 10}
                                onClick={() => this.onClickBlessMinus()}>-
                        </button>
                    </div>

                    <div id="curse" style={{display: 'flex', lineHeight: '40px'}}>
                        <button className="button-plus-minus" disabled={curseLeft <= 0}
                                onClick={() => this.onClickCursePlus()}>+
                        </button>
                        <text>Curse Cards Left: {curseLeft}</text>
                        <button className="button-plus-minus" disabled={curseLeft >= 10}
                                onClick={() => this.onClickCurseMinus()}>-
                        </button>
                    </div>
                </div>
            </div>
        )
    }
}

class Deck extends Component {
    get_cards() {
        if (this.props.hidden) {
            return this.props.cards.map(
                (val, idx) =>
                    <Card key={idx} fullName={cardName[val]}/>
            );
        }
        return this.props.cards.map(
            (val, idx) =>
                <Card key={idx} value={val} fullName={cardName[val]}> </Card>
        );
    }

    render() {
        let cards = this.get_cards();

        return (
            <div style={{justifyContent: "flex-start"}}
                 className="attack-deck">
                <div>{this.props.name}</div>
                <div style={{display: "flex", flexDirection: "row", flexWrap: "wrap"}}>{cards}</div>
            </div>
        )
    }
}

function Card(props) {
    return (
        <div className="attack-card"
             style={{flexDirection: "row", textAlign: "top"}} card-hover={props.fullName}>
            <span>{props.value}</span>
        </div>

    )
}

export default AttackModifier;