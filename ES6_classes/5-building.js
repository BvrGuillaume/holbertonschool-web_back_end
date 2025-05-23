/* eslint-disable */
export default class Building {
	constructor(sqft) {
		this._sqft = sqft;
		if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
			throw new Error('Class extending Building must override evacuationWarningMessage');
		}
	}

	get sqft() {
		return this._sqft;
	}

	set sqft(value){
		if (typeof value !== 'number') {
			throw new TypeError('sqft must be a number');
		}
		this._sqft = value;
	}
}
