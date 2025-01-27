<br />
<p align="center">
  <a href="https://github.com/alaksatti/BrokeAsF">
  </a>

  <h1 align="center">BrokeAsF</h1>

  <p align="center">
    BrokeAsF is a simple web application aimed to provide users with locations offering free meals near them in real time in the San Francisco area. WORK IN PROGRESS!! 
     <br />
    <a href="https://brokeasf.com"><strong>Check out the site! »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alaksatti/BrokeAsF/issues">Report Bug</a>
    ·
    <a href="https://github.com/alaksatti/BrokeAsF/issues">Request Feature</a>
  </p>
</p>



## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
* [Data Model](#data-model)
* [Why the Ambiguous Design](#why-the-ambiguous-design)
* [How Does it Work?](how-does-it-work)
* [Roadmap](#roadmap)
* [Covid-19 Impacts](#covid--19-impacts)

## About The Project

There is a large homeless population in the San Francisco, California area, specifially in the Tenderloin neighborhood of SF. It is no secret that hunger is a dominating issue among the homeless, however, hunger is not unique to homeless. Hunger has no face and has varying degrees. Considering the high standard of living in San Francisco, the issue of hunger may actually be more prevalent than expected. For many people, every dollar makes a difference.For some going out to eat or for a cup of coffee with coworkers or peers may require a quick calculation of their funds. Some may even have to skip meals because they cannot afford to eat. And while some people would enjoy a free meal, others require it. BrokeAsF is for these people. 

BrokeAsF is a simple web application aimed to provide users with locations offering free meals near them in real time in the San Francisco area.

** Please note Broke AsF is a work in progress, project will resume once events become more available  ** 

### Built With

* HTML
* CSS
* Javascript
* Three.js
* Google Maps API
* Google Places API
* Google Geolocation API
* SF Funcheap API (pending)
* SF Services API (pending)
* Events API (pending)

--More to come--


## Getting Started
1. Go to the site <a href="https://brokeasf.com"><strong>BrokeAsF.com</strong></a>.

2. Accept permissions to access your location.  
** Dont worry your data is not stored! ** 

3. Scroll down to the map.

<b>Thats it!</b> 
<br />
<br />
<p align="center">
  <img src="https://github.com/alaksatti/BrokeAsF/blob/master/images/BrokeAsF%20Screenshot.png">
</p><br />
<br />
***Your location is marked with the pedestrian icon and the locations offered are marked with red markers. You can click on the locations for addresses and more information i.e. food offered.




## Data Model
<br />

<p align="center">
  <img src="https://github.com/alaksatti/BrokeAsF/blob/master/images/datamodel.png">
</p><br />
<br />
<br>

## Why the Ambiguous Design?

Special consideration was taken into account for the design of the web application. Because people who need to use the app might feel embarassed about needing to use it, I did not want it to be obvious what this app was offering immediatley. This is so that someone passing by the screen of someone using the app would not be able to know that this person is looking for a meal. It is a way to maintain the privacy of the user and give them some consideration in regards to their situation.  In addition I  did not want the app to look like a 'broke app meant for broke people' as that may reinforce negative thoughts in the minds of those using the app. 


## How Does it Work?
BrokeAsF takes advantage of regularly occuring events in San Francisco that offer food/meals. These events are all over SF and are offered at a variety of times. Many times these events are FREE, most probably as a method to draw people to their events. The locations to these events are accessed through APIs. Making this connection helps event planners fill up their events with people and helps people learn new things i.e. at tech events, while also getting a free meal. Although noted, this can have some unintended consequences.

 
## RoadMap

* Currently BrokeAsF only services the San Francisco, CA area. However, in the future there are plans to expand to other locations in need as well as create a mobile version of the application.



## Covid-19 Impacts

Because BrokeAsF relies heavily on events for locations and because events have largely been cancelled due to the Covid-19 pandemic. Hard coded locations available for the time being offered from social services provided in the SF area. Once events become more readily available, work will resume to offer locations via API calls. 

<!--
## Changes to Technology
BrokeAsF is built using only front-end technology and APIs. Changes will be made to the architecture to the webapp to allow for a more robust application that would allow for more data to be collected. 
--!>

