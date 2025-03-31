/* eslint-disable */
export default function cleanSet (set, startString) {
	if (!startString || typeof startString !== 'string') {
		return '';
//Si startString est une chaîne vide (''), la fonction doit retourner une chaîne vide
	  }
	
	  return Array.from(set)
	  //Array.from(set) convertit le Set en un tableau,qui permet d'utiliser des méthodes filter(), map() et join()
	  //slice(startString.length) enlève startString au début de chaque valeur
		.filter((value) => value.startsWith(startString))
		.map((value) => value.slice(startString.length))
		.join('-');
//join('-') concatène tous les éléments du tableau avec un - entre eux
}
