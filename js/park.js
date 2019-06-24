// 1. API & Search Component Initialization

const appKey = "kuM6fs4DFwB9r2u3YIXynuYBqjD54WyB7zDc3Qvl";

let searchInput = document.getElementById("search-input");
let searchSubmitKey1 = document.getElementById("search-submit-key1");
let searchSubmitKey2 = document.getElementById("search-submit-key2");
let searchSubmitName = document.getElementById("search-submit-name");

searchSubmitKey1.addEventListener("click", function () {
    park.innerHTML = "<img src=\"images/lightgallery/loading.gif\">"
    urlBuilder(1);
});
searchSubmitKey2.addEventListener("click", function () {
    park.innerHTML = "<img src=\"images/lightgallery/loading.gif\">"
    urlBuilder(1);
});
searchSubmitName.addEventListener("click", function () {
    park.innerHTML = "<img src=\"images/lightgallery/loading.gif\">"
    urlBuilder(2);
});
searchInput.addEventListener("keyup", inputLogger);

park = document.getElementById("park-name");
let parkdesc = document.getElementById("park-desc");
start = 0;

// 2. URL Building
function inputLogger(event) {
    if (event.key === "Enter") {
        park.innerHTML = "<img src=\"images/lightgallery/loading.gif\">"
        urlBuilder(1);
    }
}

function urlBuilder(num, desPark) {
    const base = "https://developer.nps.gov/api/v1/parks?"
    var limit = "10"
    e = document.getElementById("state-select");
    state = e.options[e.selectedIndex].value;


    start = 0;

    var f = document.getElementById("des-select");
    var designation = f.options[f.selectedIndex].value;


    clearContent = true;
    loadButton = true;

    if (num != 2) {
        if (desPark === undefined) {
            if (designation != "") {
                designationSetup(num);
                return;
            }
            var parkval = document.getElementById("park-select");
        } else {
            parkval = desPark;
            clearContent = false;
            loadButton = false;
        }
    }

    if (num == 2) {
        var parkval = document.getElementById("park-select");
    }

    if (num == 1) {
        searchLink = base + "limit=" + limit + "&start=" + start + "&stateCode=" + state + "&q=" + searchInput.value + "&api_key=" + appKey;
    } else {
        searchLink = base + "limit=" + limit + "&start=" + start + "&parkCode=" + parkval.value + "&api_key=" + appKey;
    }


    xmlRequest(searchLink, mainFunction);
}

function designationSetup(num) {
    park.innerHTML = "";
    var f = document.getElementById("des-select");
    var designation = f.options[f.selectedIndex].value;
    var opt = 0;
    var btn = document.createElement("button");
    btn.innerHTML = "load more";

    var nodeArray = [].slice.call(document.querySelectorAll("select.chosen option[data-value=" + CSS.escape(designation) + "]"));

    if (state != "") {
        opt = 1;
        var des_statesArray = [];
        for (var j in nodeArray) {
            if (nodeArray[j].getAttribute('data-state').includes(state)) {
                des_statesArray.push(nodeArray[j]);
            }
        }
    } else if (searchInput.value != "") {
        opt = 2;
        var des_searchArray = [];
        for (var x in nodeArray) {
            if (nodeArray[x].text.toLowerCase().includes(searchInput.value.toLowerCase())) {
                des_searchArray.push(nodeArray[x]);
            }
        }
    }

    if (state != "" && searchInput.value != "") {
        opt = 3;
        var des_allArray = [];
        for (var q in des_statesArray) {
            if (des_statesArray[q].text.toLowerCase().includes(searchInput.value.toLowerCase())) {
                des_allArray.push(des_statesArray[q]);
            }
        }
    }

    if (opt == 0) {
        clearContent = false;
        for (var y in nodeArray) {
            urlBuilder(3, nodeArray[y]);
        }
    }

    if (opt == 1) {
        clearContent = false;
        if (des_statesArray.length < 1) {
            // $('#park-name').load(document.URL +  '#park-name', function() {
            //     $('#loaderScreen').hide();
            // });
            park.innerHTML = "no parks found";
        }
        for (var y in des_statesArray) {
            urlBuilder(3, des_statesArray[y]);
        }
    }

    if (opt == 2) {
        clearContent = false;
        if (des_searchArray.length < 1) {
            // $('#park-name').load(document.URL +  '#park-name', function() {
            //     $('#loaderScreen').hide();
            // });
            park.innerHTML = "no parks found";
        }
        for (var y in des_searchArray) {
            urlBuilder(3, des_searchArray[y]);
        }
    }

    if (opt == 3) {
        clearContent = false;
        if (des_allArray.length < 1) {
            // $('#park-name').load(document.URL +  '#park-name', function() {
            //     $('#loaderScreen').hide();
            // });
            park.innerHTML = "no parks found";
        }
        for (var y in des_allArray) {
            urlBuilder(3, des_allArray[y]);
        }
    }
}

// main results
function mainFunction(response) {
    if (clearContent == true) {
        park.innerHTML = "";
    }
    let d = JSON.parse(response);
    document.getElementById("result-desc").style.display = "none";

    for (var i in d.data) {
        var parkname = document.createElement("h2");
        parkname.innerHTML = d.data[i].fullName + " ";
        parkname.className = "pname";
        park.appendChild(parkname);

        var tags = document.createElement("h4");
        if (d.data[i].designation != "") {
            tags.innerHTML = d.data[i].states + "\t|\t" + d.data[i].designation + "<br>";
        } else {
            tags.innerHTML = d.data[i].states + "<br>";
        }
        tags.className = "tags"
        park.appendChild(tags);


        var parkdesc = document.createElement("p");
        parkdesc.innerHTML = d.data[i].description + "<br>";
        parkdesc.style.textAlign = "left";
        park.appendChild(parkdesc);

        var line = document.createElement("hr")
        park.appendChild(line)
    }

    var total = d.total;

    if (loadButton == true) {
        if (start < total) {
            var loadMore = document.createElement("button");
            loadMore.innerHTML = "Load More";
            loadMore.className = "loadMoreButton";
            loadMore.addEventListener("click", function (e) {
                // $('#loaderScreen').show();
                this.remove();
                load();
            });
            park.appendChild(loadMore);
        } else {
            var noMore = document.createElement("p");
            noMore.innerHTML = "No More Results";
            park.appendChild(noMore);
        }
    }

    // MODAL JS

    var modal = document.getElementById("myModal");
    headers = document.getElementsByTagName("h2");
    var span = document.getElementsByClassName("close")[0];

    for (var i = headers.length - 1; i >= 0; i--) {
        headers[i].onclick = function () {
            modal.style.display = "block";
            var name = this.innerText || this.textContent;
            convert(name, true);
        }
    }

    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

}

function load() {
    var loc = searchLink.lastIndexOf("start=");
    start += 10;
    searchLink = searchLink.substring(0, loc) + "start=" + start + "&" + searchLink.substring(loc + 8);
    clearContent = false;
    xmlRequest(searchLink, mainFunction);
}

// Rendering data
function render(response) {

    let d = JSON.parse(response);
    var title = document.getElementById("park-title");
    var tags = document.getElementById("tags");
    var desc = document.getElementById("park-description");
    var dir = document.getElementById("directions");
    var site = document.getElementById("website");

    title.innerHTML = d.data[0].fullName;
    if (d.data[0].designation != "") {
        tags.innerHTML = d.data[0].states + "\t | \t" + d.data[0].designation;
    } else {
        tags.innerHTML = d.data[0].states;
    }
    desc.innerHTML = d.data[0].description;
    dir.innerHTML = d.data[0].directionsInfo;
    site.innerHTML = "<img src=\"svg/website.svg\">   " + '<a target="_blank" href=' + d.data[0].url + '>' + d.data[0].url + '</a>';
    $('.modal-content').load(document.URL +  '.modal-content', function() {
                $('#modalLoader').hide();
    });
}

function getGeneral(name) {
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, render);
}

function addressRender(response) {
    let d = JSON.parse(response);
    var address = document.getElementById("addresses");
    address.innerHTML = "";
    for (i in d.data[0].addresses) {
        if (d.data[0].addresses[i].type === "Physical") {
            address.innerHTML = d.data[0].addresses[i].line1 + " " + d.data[0].addresses[i].line2 + " " + d.data[0].addresses[i].line3 +
                ", " + d.data[0].addresses[i].city + ", " + d.data[0].addresses[i].stateCode + " " + d.data[0].addresses[i].postalCode;
        }
    }

}

function getAddresses(name) {
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=addresses&api_key=" + appKey;
    xmlRequest(url, addressRender);
}

function contactRender(response) {
    let d = JSON.parse(response);
    var contact = document.getElementById("contact");
    contact.innerHTML = "";
    var info = d.data[0].contacts.phoneNumbers[0].phoneNumber;
    var res = info.replace(/\D/g, '');
    res = "(" + res.substring(0, 3) + ") " + res.substring(3, 6) + "-" + res.substring(6, 10);
    contact.innerHTML = "<img src=\"svg/telephone-black-14.svg\">   " + res;
    var email = document.getElementById("email");
    email.innerHTML = "<img src=\"svg/post-office-black-14.svg\">   " + d.data[0].contacts.emailAddresses[0].emailAddress;
}

function getContacts(name) {
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=contacts&api_key=" + appKey;
    xmlRequest(url, contactRender);
}

function hourRender(response) {
    let d = JSON.parse(response);
    var hours = document.getElementById("hours");
    hours.innerHTML = "";
    days = d.data[0].operatingHours[0].standardHours;
    for (var i in days) {
        console.log(i);
    }
    monday = document.createElement('p');
    monday.innerHTML = "Monday: " + days['monday'];
    hours.appendChild(monday);
    tuesday = document.createElement('p');
    tuesday.innerHTML = "Tuesday: " + days['tuesday'];
    hours.appendChild(tuesday);
    wednesday = document.createElement('p');
    wednesday.innerHTML = "Wednesday: " + days['wednesday'];
    hours.appendChild(wednesday);
    thursday = document.createElement('p');
    thursday.innerHTML = "Thursday: " + days['thursday'];
    hours.appendChild(thursday);
    friday = document.createElement('p');
    friday.innerHTML = "Friday: " + days['friday'];
    hours.appendChild(friday);
    saturday = document.createElement('p');
    saturday.innerHTML = "Saturday: " + days['saturday'];
    hours.appendChild(saturday);
    sunday = document.createElement('p');
    sunday.innerHTML = "Sunday: " + days['sunday'];
    hours.appendChild(sunday);
}

function getHours(name) {
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=operatingHours&api_key=" + appKey;
    xmlRequest(url, hourRender);
}

function alertRender(response) {
    let d = JSON.parse(response);
    var alerts = document.getElementById("alerts");
    alerts.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        alerts.appendChild(line);

        var tag = document.createElement("img");
        var cat = d.data[i].category;
        if (cat === "Information" || cat === "") {
            tag.src = "images/info.png";
            tag.width = "14";
        }
        if (cat === "Park Closure") {
            tag.src = "svg/construction-black-14.svg"
        }
        if (cat === "Caution") {
            tag.src = "svg/safety-caution-alerts-black-14.svg"
        }
        alerts.appendChild(tag);

        var alertName = document.createElement("h3");
        alertName.innerHTML = "&emsp;" + d.data[i].title;
        alertName.style.display = "inline-block";
        alerts.appendChild(alertName);

        var desc = document.createElement("p");
        desc.innerHTML = d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        alerts.appendChild(desc);

        if (d.data[i].url != "") {
            var link = document.createElement("p")
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            alerts.appendChild(link);
        }
    }

    if (alerts.innerHTML === "") {
        alerts.innerHTML = "<br><br><br><br><img src=\"svg/safety-caution-alerts-black-30.svg\"> <br> no alerts found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL + '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getAlerts(name) {
    url = "https://developer.nps.gov/api/v1/alerts?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, alertRender);
}


function articleRender(response) {
    let d = JSON.parse(response);
    var articles = document.getElementById("articles");
    articles.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        articles.appendChild(line);

        var articleName = document.createElement("h3");
        articleName.innerHTML = d.data[i].title + "<br>";
        articles.appendChild(articleName);

        var img = document.createElement("img");
        img.src = d.data[i].listingimage.url;
        img.style.width = "10%";
        img.style.marginRight = "30px";
        img.style.display = "inline-block";
        articles.appendChild(img);

        var desc = document.createElement("p");
        if (d.data[i].url != "") {
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        } else {
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        articles.appendChild(desc);
    }

    if (articles.innerHTML === "") {
        articles.innerHTML = "<br><br><br><br><img src=\"svg/brochure-black-30.svg\"> <br> no articles found <br><br><br><br> ";

    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });

}

function getArticles(name) {
    url = "https://developer.nps.gov/api/v1/articles?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, articleRender);
}

function campRender(response) {
    let d = JSON.parse(response);
    var camp = document.getElementById("campgrounds");
    camp.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        camp.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].name + "<br>";
        camp.appendChild(name);

        var desc = document.createElement("p");
        desc.innerHTML = d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        camp.appendChild(desc);

        var access = document.createElement("h4");
        access.innerHTML = "Accessibility";
        access.style.textAlign = "left";
        camp.appendChild(access);

        if (d.data[i].accessibility.wheelchairaccess != "") {
            var wheelchair = document.createElement("p");
            wheelchair.innerHTML = d.data[i].accessibility.wheelchairaccess;
            wheelchair.style.textAlign = "left";
            camp.appendChild(wheelchair);
        }

        var rv = document.createElement("p");
        rv.innerHTML = "RVs Allowed: " + d.data[i].accessibility.rvallowed;
        rv.style.textAlign = "left";
        camp.appendChild(rv);

        if (d.data[i].accessibility.internetinfo != "") {
            var internet = document.createElement("p");
            internet.innerHTML = d.data[i].accessibility.internetinfo;
            internet.style.textAlign = "left";
            camp.appendChild(internet);
        }

        if (d.data[i].accessibility.cellphoneinfo != "") {
            var cellphone = document.createElement("p");
            cellphone.innerHTML = d.data[i].accessibility.cellphoneinfo;
            cellphone.style.textAlign = "left";
            camp.appendChild(cellphone);
        }

        if (d.data[i].accessibility.adainfo != "") {
            var ada = document.createElement("p");
            ada.innerHTML = "Additional Info: " + d.data[i].accessibility.adainfo;
            ada.style.textAlign = "left";
            camp.appendChild(ada);
        }

        var amen = document.createElement("h4");
        amen.innerHTML = "Amenities";
        amen.style.textAlign = "left";
        camp.appendChild(amen);

        if (d.data[i].amenities.trashrecyclingcollection != "") {
            var trash = document.createElement("p");
            trash.innerHTML = "Trash & Recycling: " + d.data[i].amenities.trashrecyclingcollection;
            trash.style.textAlign = "left";
            camp.appendChild(trash);
        }

        if (d.data[i].amenities.internetconnectivity != "") {
            var inter = document.createElement("p");
            inter.innerHTML = "Internet Connectivity: " + d.data[i].amenities.internetconnectivity;
            inter.style.textAlign = "left";
            camp.appendChild(inter);
        }

        if (d.data[i].amenities.cellphonereception != "") {
            var cp = document.createElement("p");
            cp.innerHTML = "Cellphone Reception: " + d.data[i].amenities.cellphonereception;
            cp.style.textAlign = "left";
            camp.appendChild(cp);
        }

        if (d.data[i].amenities.laundry != "") {
            var laund = document.createElement("p");
            laund.innerHTML = "Laundry: " + d.data[i].amenities.laundry;
            laund.style.textAlign = "left";
            camp.appendChild(laund);
        }

        if (d.data[i].amenities.iceavailableforsale != "") {
            var ice = document.createElement("p");
            ice.innerHTML = "Ice Available For Sale: " + d.data[i].amenities.iceavailableforsale;
            ice.style.textAlign = "left";
            camp.appendChild(ice);
        }

        if (d.data[i].amenities.firewoodforsale != "") {
            var fire = document.createElement("p");
            fire.innerHTML = "Firewood For Sale: " + d.data[i].amenities.firewoodforsale;
            fire.style.textAlign = "left";
            camp.appendChild(fire);
        }

        if (d.data[i].amenities.foodstoragelockers != "") {
            var food = document.createElement("p");
            food.innerHTML = "Food Storage Lockers: " + d.data[i].amenities.foodstoragelockers;
            food.style.textAlign = "left";
            camp.appendChild(food);
        }
    }

    if (camp.innerHTML === "") {
        camp.innerHTML = "<br><br><br><br><img src=\"svg/campfire-black-30.svg\"> <br> no campgrounds found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getCampgrounds(name) {
    url = "https://developer.nps.gov/api/v1/campgrounds?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, campRender);
}


function eventRender(response) {
    let d = JSON.parse(response);
    var events = document.getElementById("events");
    events.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        events.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        events.appendChild(name);

        var tags = document.createElement("p");
        var tagarray = ["", "", "", ""];
        if (d.data[i].isrecurring.toLowerCase() === "true") {
            tagarray[0] = "Recurring";
        }
        if (d.data[i].isfree.toLowerCase() === "true") {
            tagarray[1] = "Free";
        }
        if (d.data[i].isregresrequired.toLowerCase() === "true") {
            tagarray[2] = "Registration Required";
        }
        if (d.data[i].isallday.toLowerCase() === "true") {
            tagarray[3] = "All-Day";
        }
        res = "";
        for (var j = 0; j < tagarray.length; j++) {
            if (tagarray[j] != "") {
                res += "<span style=\"border: 1px solid blue; padding: 3px; margin-right: 5px; border-radius: 40px; \">" + tagarray[j] + "</span>";
            }
        }
        tags.innerHTML = res;
        events.appendChild(tags);

        var loc = document.createElement("p");
        loc.innerHTML = "<img src=\"svg/marker.svg\">   " + d.data[i].location + "<br>";
        loc.style.textAlign = "left";
        events.appendChild(loc);

        var date = document.createElement("p");
        var res_d = d.data[i].date;
        res_d = res_d.substring(5, 7) + "/" + res_d.substring(8, 10) + "/" + res_d.substring(0, 4);
        date.innerHTML = "<img src=\"svg/calendar-events-black-14.svg\">   " + res_d + "<br>";
        date.style.textAlign = "left";
        events.appendChild(date);

        var time = document.createElement("p");
        var start = d.data[i].times[0].timestart;
        var end = d.data[i].times[0].timeend;
        res_t = start + " - " + end;
        time.innerHTML = "<img src=\"svg/clock.svg\">   " + res_t + "<br><br>";
        time.style.textAlign = "left";
        events.appendChild(time);

        var desc = document.createElement("p");
        desc.innerHTML = "<h4><u>Description</u></h4>" + d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        events.appendChild(desc);
    }

    if (events.innerHTML === "") {
        events.innerHTML = "<br><br><br><br><img src=\"svg/calendar-events-black-30.svg\"> <br> no events found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getEvents(name) {
    url = "https://developer.nps.gov/api/v1/events?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, eventRender);
}


function lessonRender(response) {
    let d = JSON.parse(response);
    var lesson = document.getElementById("lessonplans");
    lesson.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        lesson.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        lesson.appendChild(name);

        var subjects = document.createElement("h5");
        var s_res = d.data[i].subject.replace(/,/g, ", ");
        subjects.innerHTML = "<u>Subject(s):</u> " + s_res + "<br>";
        subjects.style.textAlign = "left";
        lesson.appendChild(subjects);

        var duration = document.createElement("h5");
        duration.innerHTML = "<u>Duration:</u> " + d.data[i].duration + "<br>";
        duration.style.textAlign = "left";
        lesson.appendChild(duration);

        var grade = document.createElement("h5");
        var g_res = d.data[i].gradelevel.replace(":", " -");
        grade.innerHTML = "<u>Grade Level:</u> " + g_res + "<br>";
        grade.style.textAlign = "left";
        lesson.appendChild(grade);

        var desc = document.createElement("p");
        var d_res = d.data[i].questionobjective.replace(/\n/g, "<br>");
        desc.innerHTML = "<b>Objective:</b><br>" + d_res + "<br>";
        desc.style.textAlign = "left";
        lesson.appendChild(desc);

        if (d.data[i].url != "") {
            var link = document.createElement("p");
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            lesson.appendChild(link);
        }
    }

    if (lesson.innerHTML === "") {
        lesson.innerHTML = "<br><br><br><br><img src=\"svg/bookstore-black-30.svg\"> <br> no lesson plans found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}


function getLessons(name) {
    url = "https://developer.nps.gov/api/v1/lessonplans?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, lessonRender);
}


function newsRender(response) {
    let d = JSON.parse(response);
    var news = document.getElementById("news");
    news.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        news.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        name.style.marginBottom = "2px";
        news.appendChild(name);

        var date = document.createElement("h6");
        time = d.data[i].releasedate;
        hour = time.substring(11, 13);
        val = parseInt(hour, 10);
        var ampm = "am";
        if (val > 12) {
            val = val - 12;
            ampm = "pm";
        }
        if (val == 0) {
            val = 12;
            ampm = "am";
        }
        if (val == 12 && time.substring(14, 16) == "00") {
            ampm = "noon";
        }


        res = time.substring(5, 7) + "-" + time.substring(8, 10) + "-" + time.substring(0, 4) + "&ensp;" + val + time.substring(13, 16) + " " + ampm;
        date.innerHTML = res;
        date.style.color = "grey";
        date.style.margin = "0";
        news.appendChild(date);

        var desc = document.createElement("p");
        desc.innerHTML = d.data[i].abstract + "<br>";
        desc.style.textAlign = "left";
        news.appendChild(desc);

        if (d.data[i].url != "") {
            var link = document.createElement("p");
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            news.appendChild(link);
        }
    }

    if (news.innerHTML === "") {
        news.innerHTML = "<br><br><br><br><img src=\"svg/newspaper-black-30.svg\"> <br> no news found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getNews(name) {
    url = "https://developer.nps.gov/api/v1/newsreleases?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, newsRender);
}


function peopleRender(response) {
    let d = JSON.parse(response);
    var people = document.getElementById("people");
    people.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        people.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        people.appendChild(name);

        var img = document.createElement("img");
        img.src = d.data[i].listingimage.url;
        img.style.width = "10%";
        img.style.marginRight = "30px";
        img.style.display = "inline-block";
        people.appendChild(img);

        var desc = document.createElement("p");
        if (d.data[i].url != "") {
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        } else {
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        people.appendChild(desc);
    }

    if (people.innerHTML === "") {
        people.innerHTML = "<br><br><br><br><img src=\"svg/family-restroom-black-30.svg\"> <br> no people found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getPeople(name) {
    url = "https://developer.nps.gov/api/v1/people?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, peopleRender);
}

function placesRender(response) {
    let d = JSON.parse(response);
    var places = document.getElementById("places");
    places.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        places.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        places.appendChild(name);

        var img = document.createElement("img");
        img.src = d.data[i].listingimage.url;
        img.style.width = "10%";
        img.style.marginRight = "30px";
        img.style.display = "inline-block";
        places.appendChild(img);

        var desc = document.createElement("p");
        if (d.data[i].url != "") {
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        } else {
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        places.appendChild(desc);
    }

    if (places.innerHTML === "") {
        places.innerHTML = "<br><br><br><br><img src=\"svg/cabin-black-30.svg\"> <br> no places found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getPlaces(name) {
    url = "https://developer.nps.gov/api/v1/places?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, placesRender);
}


function vcRender(response) {
    let d = JSON.parse(response);
    var vc = document.getElementById("visitorcenters");
    vc.innerHTML = "";

    for (var i = 0; i < d.data.length; i++) {
        var line = document.createElement("hr");
        vc.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].name + "<br>";
        vc.appendChild(name);

        var desc = document.createElement("p");
        desc.innerHTML = "<h4><u>Description</u></h4>" + d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        vc.appendChild(desc);

        if (d.data[i].directionsInfo != "") {
            var dir = document.createElement("p");
            dir.innerHTML = "<h4><u>Directions</u></h4>" + d.data[i].directionsInfo + "<br>";
            dir.style.textAlign = "left";
            vc.appendChild(dir);
        }

        if (d.data[i].url != "") {
            var link = document.createElement("p");

            link.innerHTML = '<img style=\"width: 14px;\" src=\"images/info.png\"><a target="_blank" href=' + d.data[i].url + '>' + ' More Information' + '</a>';
            link.style.textAlign = "left";
            vc.appendChild(link);
        }
    }

    if (vc.innerHTML === "") {
        vc.innerHTML = "<br><br><br><br><img src=\"svg/visitor-center-black-30.svg\"> <br> no places found <br><br><br><br> ";
    }

    $('.modal-content').load(document.URL +  '.modal-content', function() {
        $('#modalLoader').hide();
    });
}

function getVC(name) {
    url = "https://developer.nps.gov/api/v1/visitorcenters?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, vcRender);
}

// tabs

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("default").click();


document.addEventListener('DOMContentLoaded', function () {
    individual();
}, false);


function xmlRequest(url, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            callback(xmlhttp.responseText);
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}