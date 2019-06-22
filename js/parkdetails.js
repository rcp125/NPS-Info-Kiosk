/*  JAVASCRIPT

Table of Contents:
    1. api and search initialization
    2. url builders
    3. rendering data

*/

// 1. API & Search Component Initialization

const appKey = "kuM6fs4DFwB9r2u3YIXynuYBqjD54WyB7zDc3Qvl";

let searchInput = document.getElementById("search-input");
let searchSubmitKey1 = document.getElementById("search-submit-key1");
let searchSubmitKey2 = document.getElementById("search-submit-key2");
let searchSubmitName = document.getElementById("search-submit-name");

searchSubmitKey1.addEventListener("click", function(){ urlBuilder(1)});
searchSubmitKey2.addEventListener("click", function(){ urlBuilder(1)});
searchSubmitName.addEventListener("click", function(){ urlBuilder(2)});
searchInput.addEventListener("keyup", inputLogger);

let park = document.getElementById("park-name");
let parkdesc = document.getElementById("park-desc");
start = 0;

// 2. URL Building
function inputLogger(event) {
    if (event.key === "Enter") {
        urlBuilder(1);
    }
}

function urlBuilder(num) {  
    const base = "https://developer.nps.gov/api/v1/parks?"
    var limit = "10"
    e = document.getElementById("state-select");
    state = e.options[e.selectedIndex].value;
    let park = document.getElementById("park-select");
    
    start = 0;

    var f = document.getElementById("des-select");
    var designation = f.options[f.selectedIndex].value;

    console.log(designation);

    if(designation != ""){
        designationSetup();
        return;
    }

    if(num == 1){
        searchLink = base + "limit=" + limit + "&start=" + start + "&stateCode=" + state + "&q=" + searchInput.value + "&api_key=" + appKey;
    }
    else{
        searchLink = base + "limit=" + limit + "&start=" + start + "&parkCode=" + park.value + "&api_key=" + appKey;
    }

    clearContent = true;

    xmlRequest(searchLink, mainFunction);                   
}

function designationSetup(){
    var nodeArray = [].slice.call(document.querySelectorAll('select.chosen option[data-value=\'National Park\']'));
        var desArray = [];
        for(var i in nodeArray){
            desArray[i] = nodeArray[i].value;
        }

    if(state != ""){
        var des_statesArray = [];
        for(var j in nodeArray){
            if (nodeArray[j].getAttribute('data-state') == state){
                des_statesArray.push(nodeArray[j]);
            }
        }
    }

    else if(searchInput.value != ""){
        var des_searchArray = [];
        for(var x in nodeArray){
            if (nodeArray[x].includes(searchInput.value)){
                des_searchArray.push(nodeArray[x]);
            }
        }
    }

    if(state != "" && searchInput.value != ""){
        var des_allArray = [];
        for(var q in des_statesArray){
            if(des_statesArray[q].includes(searchInput.value)){
                des_allArray.push(des_statesArray[q]);
            }
        }
    }
}

// main results
function mainFunction(response) {
    if(clearContent == true){
        park.innerHTML = "";
    }
    let d = JSON.parse(response);
    document.getElementById("result-desc").style.display = "none";

    for (var i in d.data){
        var parkname = document.createElement("h2");
        parkname.innerHTML = d.data[i].fullName + " ";
        parkname.className = "pname";
        park.appendChild(parkname);

        var tags = document.createElement("h4");
        if(d.data[i].designation != ""){
            tags.innerHTML = d.data[i].states + "\t|\t" + d.data[i].designation + "<br>";
        }
        else{
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

    if(start < total){
        var loadMore = document.createElement("button");
        loadMore.innerHTML = "Load More";
        loadMore.className = "loadMoreButton";
        loadMore.addEventListener("click", function(e) {
            this.remove();
            load();
        });
        park.appendChild(loadMore);
    }
    else{
        var noMore = document.createElement("p");
        noMore.innerHTML = "No More Results";
        park.appendChild(noMore);
    }

    // 

    // alert(document.querySelectorAll('select.chosen option[data-value=\'National Park\']').text);

    

        // MODAL JS

        var modal = document.getElementById("myModal");
        headers = document.getElementsByTagName("h2");
        var span = document.getElementsByClassName("close")[0];

        for(var i = headers.length - 1; i >= 0; i--){
            headers[i].onclick = function() {
                modal.style.display = "block";
                var name = this.innerText || this.textContent;
                convert(name, true);
            }
        }

        span.onclick = function() {
            modal.style.display = "none";
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
}

function load(){
    var loc = searchLink.lastIndexOf("start=");
    start += 10;
    searchLink = searchLink.substring(0,loc) + "start=" + start + "&" + searchLink.substring(loc+8);
    clearContent = false;
    xmlRequest(searchLink, mainFunction);
}

// Rendering data
function render(response){

    let d = JSON.parse(response);
    var title = document.getElementById("park-title");
    var tags = document.getElementById("tags");
    var desc = document.getElementById("park-description");
    var dir = document.getElementById("directions");
    var site = document.getElementById("website");

    title.innerHTML = d.data[0].fullName;
    tags.innerHTML = d.data[0].states + "\t | \t" + d.data[0].designation;
    desc.innerHTML = d.data[0].description;
    dir.innerHTML = d.data[0].directionsInfo;
    site.innerHTML = "<img src=\"svg/website.svg\">   " + '<a target="_blank" href=' + d.data[0].url + '>' + d.data[0].url + '</a>';
}

function getGeneral(name){
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, render);
}

function addressRender(response){
    let d = JSON.parse(response);
    var address = document.getElementById("addresses");
    address.innerHTML = "";
    for(i in d.data[0].addresses){
        if(d.data[0].addresses[i].type === "Physical"){
            address.innerHTML = d.data[0].addresses[i].line1 + " " + d.data[0].addresses[i].line2 + " " + d.data[0].addresses[i].line3
            + ", " + d.data[0].addresses[i].city + ", " + d.data[0].addresses[i].stateCode + " " + d.data[0].addresses[i].postalCode;
        }
    }
    
}

function getAddresses(name){
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=addresses&api_key=" + appKey;
    xmlRequest(url, addressRender);
}

function contactRender(response){
    let d = JSON.parse(response);
    var contact = document.getElementById("contact");
    contact.innerHTML = "";
    var info = d.data[0].contacts.phoneNumbers[0].phoneNumber;
    var res = info.replace(/\D/g,'');
    res = "(" + res.substring(0,3) + ") " + res.substring(3,6) + "-" + res.substring(6,10); 
    contact.innerHTML = "<img src=\"svg/telephone-black-14.svg\">   " + res;
    var email = document.getElementById("email");
    email.innerHTML = "<img src=\"svg/post-office-black-14.svg\">   " + d.data[0].contacts.emailAddresses[0].emailAddress;
}

function getContacts(name){
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=contacts&api_key=" + appKey;
    xmlRequest(url, contactRender);
}

function hourRender(response){
    let d = JSON.parse(response);
    var hours = document.getElementById("hours");
    hours.innerHTML = "";
    days = d.data[0].operatingHours[0].standardHours;
    for(var i in days){
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

function getHours(name){
    url = "https://developer.nps.gov/api/v1/parks?parkCode=" + name + "&fields=operatingHours&api_key=" + appKey;
    xmlRequest(url, hourRender);
}

function alertRender(response){
    let d = JSON.parse(response);
    var alerts = document.getElementById("alerts");
    alerts.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
        var line = document.createElement("hr");
        alerts.appendChild(line);

        var tag = document.createElement("img");
        var cat = d.data[i].category;
        if(cat === "Information" || cat === ""){
            tag.src = "images/info.png";
            tag.width = "14";
        }
        if(cat === "Park Closure"){
            tag.src = "svg/construction-black-14.svg"
        }
        if(cat === "Caution"){
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

        if(d.data[i].url != ""){
            var link = document.createElement("p")
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            alerts.appendChild(link);
        }
    } 

    if(alerts.innerHTML === ""){
        alerts.innerHTML = "<br><br><br><br><img src=\"svg/safety-caution-alerts-black-30.svg\"> <br> no alerts found <br><br><br><br> ";
    }
}

function getAlerts(name){
    url = "https://developer.nps.gov/api/v1/alerts?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, alertRender);
}


function articleRender(response){
    let d = JSON.parse(response);
    var articles = document.getElementById("articles");
    articles.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
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
        if(d.data[i].url != ""){
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        }
        else{
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        articles.appendChild(desc);
    }

    if(articles.innerHTML === ""){
        articles.innerHTML = "<br><br><br><br><img src=\"svg/brochure-black-30.svg\"> <br> no articles found <br><br><br><br> ";

    }

}

function getArticles(name){
    url = "https://developer.nps.gov/api/v1/articles?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, articleRender);
}

function campRender(response){
    let d = JSON.parse(response);
    var camp = document.getElementById("campgrounds");
    camp.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
        var line = document.createElement("hr");
        camp.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].name + "<br>";
        camp.appendChild(name);

        var desc = document.createElement("p");
        desc.innerHTML = d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        camp.appendChild(desc);
    } 

    if(camp.innerHTML === ""){
        camp.innerHTML = "<br><br><br><br><img src=\"svg/campfire-black-30.svg\"> <br> no campgrounds found <br><br><br><br> ";
    }
}

function getCampgrounds(name){
    url = "https://developer.nps.gov/api/v1/campgrounds?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, campRender);
}



function eventRender(response){
    let d = JSON.parse(response);
    var events = document.getElementById("events");
    events.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
        var line = document.createElement("hr");
        events.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        events.appendChild(name);

        var tags = document.createElement("p");
        var tagarray = ["", "", "", ""];
        if(d.data[i].isrecurring.toLowerCase() === "true"){
            tagarray[0] = "Recurring";
        }
        if(d.data[i].isfree.toLowerCase() === "true"){
            tagarray[1] = "Free";
        }
        if(d.data[i].isregresrequired.toLowerCase() === "true"){
            tagarray[2] = "Registration Required";
        }
        if(d.data[i].isallday.toLowerCase() === "true"){
            tagarray[3] = "All-Day";
        }
        res = "";
        for(var j = 0; j < tagarray.length; j++){
            if(tagarray[j] != ""){
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
        res_d = res_d.substring(5,7) + "/" + res_d.substring(8,10) + "/" + res_d.substring(0,4);
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

    if(events.innerHTML === ""){
        events.innerHTML = "<br><br><br><br><img src=\"svg/calendar-events-black-30.svg\"> <br> no events found <br><br><br><br> ";
    }
}

function getEvents(name){
    url = "https://developer.nps.gov/api/v1/events?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, eventRender);
}


function lessonRender(response){
    let d = JSON.parse(response);
    var lesson = document.getElementById("lessonplans");
    lesson.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
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

        if(d.data[i].url != ""){
            var link = document.createElement("p");
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            lesson.appendChild(link);
        } 
    } 

    if(lesson.innerHTML === ""){
        lesson.innerHTML = "<br><br><br><br><img src=\"svg/bookstore-black-30.svg\"> <br> no lesson plans found <br><br><br><br> ";
    }
}


function getLessons(name){
    url = "https://developer.nps.gov/api/v1/lessonplans?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, lessonRender);
}


function newsRender(response){
    let d = JSON.parse(response);
    var news = document.getElementById("news");
    news.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
        var line = document.createElement("hr");
        news.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].title + "<br>";
        name.style.marginBottom = "2px";
        news.appendChild(name);

        var date = document.createElement("h6");
        time = d.data[i].releasedate;
        hour = time.substring(11,13);
        val = parseInt(hour, 10);
        var ampm = "am";
        if(val > 12){
            val = val - 12;
            ampm = "pm";
        }
        if(val == 0){
            val = 12;
            ampm = "am";
        }
        if(val == 12 && time.substring(14,16) == "00"){
            ampm = "noon";
        }


        res = time.substring(5,7) + "-" + time.substring(8,10) + "-" + time.substring(0,4) + "&ensp;" + val + time.substring(13,16) + " " + ampm;
        date.innerHTML = res;
        date.style.color = "grey";
        date.style.margin = "0";
        news.appendChild(date);

        var desc = document.createElement("p");
        desc.innerHTML = d.data[i].abstract + "<br>";
        desc.style.textAlign = "left";
        news.appendChild(desc);

        if(d.data[i].url != ""){
            var link = document.createElement("p");
            link.innerHTML = '<a target="_blank" href=' + d.data[i].url + '>' + 'Read More' + '</a>';
            link.style.textAlign = "left";
            news.appendChild(link);
        } 
    } 

    if(news.innerHTML === ""){
        news.innerHTML = "<br><br><br><br><img src=\"svg/newspaper-black-30.svg\"> <br> no news found <br><br><br><br> ";
    }
}

function getNews(name){
    url = "https://developer.nps.gov/api/v1/newsreleases?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, newsRender);
}


function peopleRender(response){
    let d = JSON.parse(response);
    var people = document.getElementById("people");
    people.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
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
        if(d.data[i].url != ""){
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        }
        else{
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        people.appendChild(desc);
    } 

    if(people.innerHTML === ""){
        people.innerHTML = "<br><br><br><br><img src=\"svg/family-restroom-black-30.svg\"> <br> no people found <br><br><br><br> ";
    }
}

function getPeople(name){
    url = "https://developer.nps.gov/api/v1/people?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, peopleRender);
}

function placesRender(response){
    let d = JSON.parse(response);
    var places = document.getElementById("places");
    places.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
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
        if(d.data[i].url != ""){
            desc.innerHTML = d.data[i].listingdescription + "<br>" + '<a target="_blank" href=' + d.data[i].url + '><br>' + 'Read More' + '</a>';
        }
        else{
            desc.innerHTML = d.data[i].listingdescription + "<br>";
        }
        desc.style.textAlign = "left";
        desc.style.display = "inline-block";
        desc.style.width = "80%";
        desc.style.marginTop = "0";
        desc.style.verticalAlign = "top";
        places.appendChild(desc);
    } 

    if(places.innerHTML === ""){
        places.innerHTML = "<br><br><br><br><img src=\"svg/cabin-black-30.svg\"> <br> no places found <br><br><br><br> ";
    }
}

function getPlaces(name){
    url = "https://developer.nps.gov/api/v1/places?parkCode=" + name + "&api_key=" + appKey;
    xmlRequest(url, placesRender);
}


function vcRender(response){
    let d = JSON.parse(response);
    var vc = document.getElementById("visitorcenters");
    vc.innerHTML = "";

    for(var i = 0; i < d.data.length; i++){
        var line = document.createElement("hr");
        vc.appendChild(line);

        var name = document.createElement("h3");
        name.innerHTML = d.data[i].name + "<br>";
        vc.appendChild(name);

        var desc = document.createElement("p");
        desc.innerHTML = "<h4><u>Description</u></h4>" + d.data[i].description + "<br>";
        desc.style.textAlign = "left";
        vc.appendChild(desc);

        if(d.data[i].directionsInfo != ""){
            var dir = document.createElement("p");
            dir.innerHTML = "<h4><u>Directions</u></h4>" + d.data[i].directionsInfo + "<br>";
            dir.style.textAlign = "left";
            vc.appendChild(dir);
        }

        if(d.data[i].url != ""){
            var link = document.createElement("p");

            link.innerHTML = '<img style=\"width: 14px;\" src=\"images/info.png\"><a target="_blank" href=' + d.data[i].url + '>' + ' More Information' + '</a>';
            link.style.textAlign = "left";
            vc.appendChild(link);
        } 
    } 

    if(vc.innerHTML === ""){
        vc.innerHTML = "<br><br><br><br><img src=\"svg/visitor-center-black-30.svg\"> <br> no places found <br><br><br><br> ";
    }
}

function getVC(name){
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


document.addEventListener('DOMContentLoaded', function() {
    individual();
}, false);


// converting name to parkCode


function xmlRequest(url, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            callback(xmlhttp.responseText);
    }
    xmlhttp.open("GET", url, true); 
    xmlhttp.send();
}
