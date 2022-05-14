console.log("Let's get this party started!");

const key = "WlA6pT650MmIpl36cMr6HMNkraYIWuRz";

async function getApi() {
  const res = await axios.get("http://api.giphy.com/v1/gifs/search", {
    params: {
      api_key: key,
      q: "burrito",
      limit: 1,
    },
  });
  const imgSrc = res.data.data[0].url;
  console.log(imgSrc);
  console.log(res);

  const btn = document.querySelector("#btn");

  btn.addEventListener("click", function () {
    const newImg = document.createElement("img");
    newImg.src = imgSrc;
    const div = document.querySelector("#container");
    div.append(newImg);
  });
}

getApi();
