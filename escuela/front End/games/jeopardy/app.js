// const startGame = document.querySelector("#start");

// startGame.addEventListener("click", start);

function start() {
	// startGame.remove();s
	const apiUrl = 'https://jservice.io/api/';
	const question = 6;
	const answer = 5;

	let categories = [];


	async function getJeopardyId() {
		const res = await axios.get(`${apiUrl}categories?count=100`);
		console.log(res);

		let ids = res.data.map((c) => c.id);
		// console.log(ids);

		// randomQ grabs 6 random id from apis

		return _.sampleSize(ids, question);
	}

	async function jeopardyCategory(valId) {
		let res = await axios.get(`${apiUrl}category?id=${valId}`);
		console.log(res)

		let val = res.data;
		// console.log(val)

		let valClue = val.clues;
		// console.log(valClue)

		let randomVal = _.sampleSize(valClue, answer);
		// console.log(randomVal)

		let clues = randomVal.map((c) => ({
			question : c.question,
			answer   : c.answer,
			showing  : null
		}));
		console.log(clues);

		return { title: res.title, clues };
	}
	
;
async function start(){
let catIds= await getJeopardyId()

categories=[]

for (let catId of catIds){
  categories.push(await jeopardyCategory(catId))
  console.log(categories)
}
} 

  ;
}

start();

// ------------------------------------------------
