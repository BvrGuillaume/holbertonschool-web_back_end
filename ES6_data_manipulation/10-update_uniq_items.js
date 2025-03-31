/* eslint-disable */
export default function unpdateUniqueItems (map) {
	//Vérification si map est bien une instance de Map
	if (!(map instanceof Map)) {
		throw new Error('Cannot process');
		//Si ce n’est pas une Map, on lance une erreur
	  }
	//Parcours de chaque entrée de la Map, vérifie chaque valeur
	  for (const [key, value] of map.entries()) {
		if (value === 1) {
		  map.set(key, 100);
		}
	  }
}
