/* eslint-disable */
export default function taskBlock(trueorFalse) {
	const task = false;
	const task2 = true;

	if (trueorFalse) {
		console.log(task, task2);
		return [task, task2];
	}

	return [task, task2];
}
