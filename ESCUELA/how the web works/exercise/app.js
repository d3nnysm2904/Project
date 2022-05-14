console.log("Let's get this party started!");


async function getApi() {
  const key = "WlA6pT650MmIpl36cMr6HMNkraYIWuRz";
  const input = document.querySelector("#input");
  const search = input.value;

  const res = await axios.get(
    "https://api.giphy.com/v1/gifs/search?api_key=WlA6pT650MmIpl36cMr6HMNkraYIWuRz&q=meme&limit=25&offset=0&rating=g&lang=en" // {
    //params: {
    // api_key: key,
    // q: search,
    // limit: 1,
    //},}
  );
  //const imgSrc = res.data.data[0].url;
  // console.log(imgSrc);
  console.log(res);
}

const btn = document.querySelector("#btn");

btn.addEventListener("click", function (e) {
  e.preventDefalut();
  const newImg = document.createElement("img");
  newImg.src = imgSrc;
  const div = document.querySelector("#container");
  div.append(newImg);

  getApi();
});