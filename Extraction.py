import urllib.request, json 


base = 'https://developer.nps.gov/api/v1/'
query = 'parks?stateCode=&limit=496&'
appid = 'kuM6fs4DFwB9r2u3YIXynuYBqjD54WyB7zDc3Qvl'

link = base + query + 'api_key=' + appid

with urllib.request.urlopen(link) as url:
    data = json.loads(url.read().decode())

    # Get unique designations
    desList = []
    for a in range(len(data['data'])):
        if data['data'][a]['designation'] not in desList:
            desList.append(data['data'][a]['designation'])

    # Get all parks
    parkList = []
    for b in range(len(data['data'])):
    	parkList.append(data['data'][b]['fullName'])

    # Get park code for each park
    parkCodeList = []
    for c in range(len(data['data'])):
    	parkCodeList.append(data['data'][c]['parkCode'])

    # Get designation for each park
    parkDesList = []
    for d in range(len(data['data'])):
    	parkDesList.append(data['data'][d]['designation'])

    # Get state for each park
    stateList = []
    for e in range(len(data['data'])):
    	stateList.append(data['data'][e]['states'])


    ### use nimble text application to append results and include in options

#######################
# Options for all parks
#######################

# <option>Abraham Lincoln Birthplace National Historical Park</option>
# <option>Acadia National Park</option>
# <option>Adams National Historical Park</option>
# <option>African American Civil War Memorial</option>
# <option>African Burial Ground National Monument</option>
# <option>Agate Fossil Beds National Monument</option>
# <option>Ala Kahakai National Historic Trail</option>
# <option>Alagnak Wild River</option>
# <option>Alaska Public Lands</option>
# <option>Alcatraz Island</option>
# <option>Aleutian Islands World War II National Historic Area</option>
# <option>Alibates Flint Quarries National Monument</option>
# <option>Allegheny Portage Railroad National Historic Site</option>
# <option>American Memorial Park</option>
# <option>Amistad National Recreation Area</option>
# <option>Anacostia Park</option>
# <option>Andersonville National Historic Site</option>
# <option>Andrew Johnson National Historic Site</option>
# <option>Aniakchak National Monument & Preserve</option>
# <option>Antietam National Battlefield</option>
# <option>Apostle Islands National Lakeshore</option>
# <option>Appalachian National Scenic Trail</option>
# <option>Appomattox Court House National Historical Park</option>
# <option>Arabia Mountain National Heritage Area</option>
# <option>Arches National Park</option>
# <option>Arkansas Post National Memorial</option>
# <option>Arlington House</option>
# <option>Assateague Island National Seashore</option>
# <option>Atchafalaya National Heritage Area</option>
# <option>Augusta Canal National Heritage Area</option>
# <option>Aztec Ruins National Monument</option>
# <option>Badlands National Park</option>
# <option>Baltimore National Heritage Area</option>
# <option>Baltimore-Washington Parkway</option>
# <option>Bandelier National Monument</option>
# <option>Belmont-Paul Women's Equality National Monument</option>
# <option>Bent's Old Fort National Historic Site</option>
# <option>Bering Land Bridge National Preserve</option>
# <option>Big Bend National Park</option>
# <option>Big Cypress National Preserve</option>
# <option>Big Hole National Battlefield</option>
# <option>Big South Fork National River & Recreation Area</option>
# <option>Big Thicket National Preserve</option>
# <option>Bighorn Canyon National Recreation Area</option>
# <option>Birmingham Civil Rights National Monument</option>
# <option>Biscayne National Park</option>
# <option>Black Canyon Of The Gunnison National Park</option>
# <option>Blackstone River Valley National Historical Park</option>
# <option>Blue Ridge National Heritage Area</option>
# <option>Blue Ridge Parkway</option>
# <option>Bluestone National Scenic River</option>
# <option>Booker T Washington National Monument</option>
# <option>Boston African American National Historic Site</option>
# <option>Boston Harbor Islands National Recreation Area</option>
# <option>Boston National Historical Park</option>
# <option>Brices Cross Roads National Battlefield Site</option>
# <option>Brown v. Board of Education National Historic Site</option>
# <option>Bryce Canyon National Park</option>
# <option>Buck Island Reef National Monument</option>
# <option>Buffalo National River</option>
# <option>Cabrillo National Monument</option>
# <option>California National Historic Trail</option>
# <option>Camp Nelson National Monument</option>
# <option>Canaveral National Seashore</option>
# <option>Cane River Creole National Historical Park</option>
# <option>Cane River National Heritage Area</option>
# <option>Canyon de Chelly National Monument</option>
# <option>Canyonlands National Park</option>
# <option>Cape Cod National Seashore</option>
# <option>Cape Hatteras National Seashore</option>
# <option>Cape Henry Memorial Part of Colonial National Historical Park</option>
# <option>Cape Krusenstern National Monument</option>
# <option>Cape Lookout National Seashore</option>
# <option>Capitol Hill Parks</option>
# <option>Capitol Reef National Park</option>
# <option>Captain John Smith Chesapeake National Historic Trail</option>
# <option>Capulin Volcano National Monument</option>
# <option>Carl Sandburg Home National Historic Site</option>
# <option>Carlsbad Caverns National Park</option>
# <option>Carter G. Woodson Home National Historic Site</option>
# <option>Casa Grande Ruins National Monument</option>
# <option>Castillo de San Marcos National Monument</option>
# <option>Castle Clinton National Monument</option>
# <option>Castle Mountains National Monument</option>
# <option>Catoctin Mountain Park</option>
# <option>Cedar Breaks National Monument</option>
# <option>Cedar Creek & Belle Grove National Historical Park</option>
# <option>César E. Chávez National Monument</option>
# <option>Chaco Culture National Historical Park</option>
# <option>Chamizal National Memorial</option>
# <option>Champlain Valley National Heritage Partnership</option>
# <option>Channel Islands National Park</option>
# <option>Charles Pinckney National Historic Site</option>
# <option>Charles Young Buffalo Soldiers National Monument</option>
# <option>Chattahoochee River National Recreation Area</option>
# <option>Chesapeake & Ohio Canal National Historical Park</option>
# <option>Chesapeake Bay</option>
# <option>Chesapeake Bay Gateways and Watertrails Network</option>
# <option>Chickamauga & Chattanooga National Military Park</option>
# <option>Chickasaw National Recreation Area</option>
# <option>Chiricahua National Monument</option>
# <option>Christiansted National Historic Site</option>
# <option>City Of Rocks National Reserve</option>
# <option>Civil War Defenses of Washington</option>
# <option>Clara Barton National Historic Site</option>
# <option>Coal National Heritage Area</option>
# <option>Colonial National Historical Park</option>
# <option>Colorado National Monument</option>
# <option>Coltsville National Historical Park</option>
# <option>Congaree National Park</option>
# <option>Constitution Gardens</option>
# <option>Coronado National Memorial</option>
# <option>Cowpens National Battlefield</option>
# <option>Crater Lake National Park</option>
# <option>Craters Of The Moon National Monument & Preserve</option>
# <option>Crossroads of the American Revolution National Heritage Area</option>
# <option>Cumberland Gap National Historical Park</option>
# <option>Cumberland Island National Seashore</option>
# <option>Curecanti National Recreation Area</option>
# <option>Cuyahoga Valley National Park</option>
# <option>David Berger National Memorial</option>
# <option>Dayton Aviation Heritage National Historical Park</option>
# <option>De Soto National Memorial</option>
# <option>Death Valley National Park</option>
# <option>Delaware & Lehigh National Heritage Corridor</option>
# <option>Delaware Water Gap National Recreation Area</option>
# <option>Denali National Park & Preserve</option>
# <option>Devils Postpile National Monument</option>
# <option>Devils Tower National Monument</option>
# <option>Dinosaur National Monument</option>
# <option>Dry Tortugas National Park</option>
# <option>Ebey's Landing National Historical Reserve</option>
# <option>Edgar Allan Poe National Historic Site</option>
# <option>Effigy Mounds National Monument</option>
# <option>Eisenhower National Historic Site</option>
# <option>El Camino Real de los Tejas National Historic Trail</option>
# <option>El Camino Real de Tierra Adentro National Historic Trail</option>
# <option>El Malpais National Monument</option>
# <option>El Morro National Monument</option>
# <option>Eleanor Roosevelt National Historic Site</option>
# <option>Ellis Island Part of Statue of Liberty National Monument</option>
# <option>Erie Canalway National Heritage Corridor</option>
# <option>Essex National Heritage Area</option>
# <option>Eugene O'Neill National Historic Site</option>
# <option>Everglades National Park</option>
# <option>Fallen Timbers Battlefield and Fort Miamis National Historic Site</option>
# <option>Federal Hall National Memorial</option>
# <option>Fire Island National Seashore</option>
# <option>First Ladies National Historic Site</option>
# <option>First State National Historical Park</option>
# <option>Flight 93 National Memorial</option>
# <option>Florissant Fossil Beds National Monument</option>
# <option>Ford's Theatre</option>
# <option>Fort Bowie National Historic Site</option>
# <option>Fort Davis National Historic Site</option>
# <option>Fort Donelson National Battlefield</option>
# <option>Fort Dupont Park</option>
# <option>Fort Foote Park</option>
# <option>Fort Frederica National Monument</option>
# <option>Fort Laramie National Historic Site</option>
# <option>Fort Larned National Historic Site</option>
# <option>Fort Matanzas National Monument</option>
# <option>Fort McHenry National Monument and Historic Shrine</option>
# <option>Fort Monroe National Monument</option>
# <option>Fort Necessity National Battlefield</option>
# <option>Fort Point National Historic Site</option>
# <option>Fort Pulaski National Monument</option>
# <option>Fort Raleigh National Historic Site</option>
# <option>Fort Scott National Historic Site</option>
# <option>Fort Smith National Historic Site</option>
# <option>Fort Stanwix National Monument</option>
# <option>Fort Sumter and Fort Moultrie National Historical Park</option>
# <option>Fort Union National Monument</option>
# <option>Fort Union Trading Post National Historic Site</option>
# <option>Fort Vancouver National Historic Site</option>
# <option>Fort Washington Park</option>
# <option>Fossil Butte National Monument</option>
# <option>Franklin Delano Roosevelt Memorial</option>
# <option>Frederick Douglass National Historic Site</option>
# <option>Frederick Law Olmsted National Historic Site</option>
# <option>Fredericksburg & Spotsylvania National Military Park</option>
# <option>Freedom Riders National Monument</option>
# <option>Friendship Hill National Historic Site</option>
# <option>Gates Of The Arctic National Park & Preserve</option>
# <option>Gateway Arch National Park</option>
# <option>Gateway National Recreation Area</option>
# <option>Gauley River National Recreation Area</option>
# <option>General Grant National Memorial</option>
# <option>George Rogers Clark National Historical Park</option>
# <option>George Washington Birthplace National Monument</option>
# <option>George Washington Carver National Monument</option>
# <option>George Washington Memorial Parkway</option>
# <option>Gettysburg National Military Park</option>
# <option>Gila Cliff Dwellings National Monument</option>
# <option>Glacier Bay National Park & Preserve</option>
# <option>Glacier National Park</option>
# <option>Glen Canyon National Recreation Area</option>
# <option>Glen Echo Park</option>
# <option>Gloria Dei Church National Historic Site</option>
# <option>Golden Gate National Recreation Area</option>
# <option>Golden Spike National Historical Park</option>
# <option>Governors Island National Monument</option>
# <option>Grand Canyon National Park</option>
# <option>Grand Portage National Monument</option>
# <option>Grand Teton National Park</option>
# <option>Grant-Kohrs Ranch National Historic Site</option>
# <option>Great Basin National Park</option>
# <option>Great Egg Harbor River</option>
# <option>Great Falls Park</option>
# <option>Great Sand Dunes National Park & Preserve</option>
# <option>Great Smoky Mountains National Park</option>
# <option>Green Springs</option>
# <option>Greenbelt Park</option>
# <option>Guadalupe Mountains National Park</option>
# <option>Guilford Courthouse National Military Park</option>
# <option>Gulf Islands National Seashore</option>
# <option>Gullah/Geechee Cultural Heritage Corridor</option>
# <option>Hagerman Fossil Beds National Monument</option>
# <option>Haleakal&#257; National Park</option>
# <option>Hamilton Grange National Memorial</option>
# <option>Hampton National Historic Site</option>
# <option>Harmony Hall</option>
# <option>Harpers Ferry National Historical Park</option>
# <option>Harriet Tubman National Historical Park</option>
# <option>Harriet Tubman Underground Railroad National Historical Park</option>
# <option>Harry S Truman National Historic Site</option>
# <option>Hawai'i Volcanoes National Park</option>
# <option>Herbert Hoover National Historic Site</option>
# <option>Historic Jamestowne Part of Colonial National Historical Park</option>
# <option>Hohokam Pima National Monument</option>
# <option>Home Of Franklin D Roosevelt National Historic Site</option>
# <option>Homestead National Monument of America</option>
# <option>Honouliuli National Historic Site</option>
# <option>Hopewell Culture National Historical Park</option>
# <option>Hopewell Furnace National Historic Site</option>
# <option>Horseshoe Bend National Military Park</option>
# <option>Hot Springs National Park</option>
# <option>Hovenweep National Monument</option>
# <option>Hubbell Trading Post National Historic Site</option>
# <option>Hudson River Valley National Heritage Area</option>
# <option>I&#241;upiat Heritage Center</option>
# <option>Ice Age Floods National Geologic Trail</option>
# <option>Ice Age National Scenic Trail</option>
# <option>Independence National Historical Park</option>
# <option>Indiana Dunes National Park</option>
# <option>Isle Royale National Park</option>
# <option>James A Garfield National Historic Site</option>
# <option>Jean Lafitte National Historical Park and Preserve</option>
# <option>Jewel Cave National Monument</option>
# <option>Jimmy Carter National Historic Site</option>
# <option>John Day Fossil Beds National Monument</option>
# <option>John Fitzgerald Kennedy National Historic Site</option>
# <option>John H. Chafee Blackstone River Valley National Heritage Corridor</option>
# <option>John Muir National Historic Site</option>
# <option>Johnstown Flood National Memorial</option>
# <option>Joshua Tree National Park</option>
# <option>Journey Through Hallowed Ground National Heritage Area</option>
# <option>Juan Bautista de Anza National Historic Trail</option>
# <option>Kalaupapa National Historical Park</option>
# <option>Kaloko-Honok&#333;hau National Historical Park</option>
# <option>Katahdin Woods and Waters National Monument</option>
# <option>Katmai National Park & Preserve</option>
# <option>Kenai Fjords National Park</option>
# <option>Kenilworth Park & Aquatic Gardens</option>
# <option>Kennesaw Mountain National Battlefield Park</option>
# <option>Keweenaw National Historical Park</option>
# <option>Kings Mountain National Military Park</option>
# <option>Klondike Gold Rush - Seattle Unit National Historical Park</option>
# <option>Klondike Gold Rush National Historical Park</option>
# <option>Knife River Indian Villages National Historic Site</option>
# <option>Kobuk Valley National Park</option>
# <option>Korean War Veterans Memorial</option>
# <option>Lake Clark National Park & Preserve</option>
# <option>Lake Mead National Recreation Area</option>
# <option>Lake Meredith National Recreation Area</option>
# <option>Lake Roosevelt National Recreation Area</option>
# <option>Lassen Volcanic National Park</option>
# <option>Lava Beds National Monument</option>
# <option>LBJ Memorial Grove on the Potomac</option>
# <option>Lewis & Clark National Historic Trail</option>
# <option>Lewis and Clark National Historical Park</option>
# <option>Lincoln Boyhood National Memorial</option>
# <option>Lincoln Home National Historic Site</option>
# <option>Lincoln Memorial</option>
# <option>Little Bighorn Battlefield National Monument</option>
# <option>Little River Canyon National Preserve</option>
# <option>Little Rock Central High School National Historic Site</option>
# <option>Longfellow House Washington's Headquarters National Historic Site</option>
# <option>Lowell National Historical Park</option>
# <option>Lower Delaware National Wild and Scenic River</option>
# <option>Lower East Side Tenement Museum National Historic Site</option>
# <option>Lyndon B Johnson National Historical Park</option>
# <option>Maggie L Walker National Historic Site</option>
# <option>Maine Acadian Culture</option>
# <option>Mammoth Cave National Park</option>
# <option>Manassas National Battlefield Park</option>
# <option>Manhattan Project National Historical Park</option>
# <option>Manzanar National Historic Site</option>
# <option>Marsh - Billings - Rockefeller National Historical Park</option>
# <option>Martin Luther King</option>
# <option>Martin Luther King</option>
# <option>Martin Van Buren National Historic Site</option>
# <option>Mary McLeod Bethune Council House National Historic Site</option>
# <option>Mesa Verde National Park</option>
# <option>Minidoka National Historic Site</option>
# <option>Minute Man National Historical Park</option>
# <option>Minuteman Missile National Historic Site</option>
# <option>Mississippi Delta National Heritage Area</option>
# <option>Mississippi Gulf National Heritage Area</option>
# <option>Mississippi Hills National Heritage Area</option>
# <option>Mississippi National River and Recreation Area</option>
# <option>Missouri National Recreational River</option>
# <option>Mojave National Preserve</option>
# <option>Monocacy National Battlefield</option>
# <option>Montezuma Castle National Monument</option>
# <option>Moores Creek National Battlefield</option>
# <option>Mormon Pioneer National Historic Trail</option>
# <option>Morristown National Historical Park</option>
# <option>Motor Cities National Heritage Area</option>
# <option>Mount Rainier National Park</option>
# <option>Mount Rushmore National Memorial</option>
# <option>Muir Woods National Monument</option>
# <option>Muscle Shoals National Heritage Area</option>
# <option>Natchez National Historical Park</option>
# <option>Natchez Trace National Scenic Trail</option>
# <option>Natchez Trace Parkway</option>
# <option>National Aviation Heritage Area</option>
# <option>National Capital Parks-East</option>
# <option>National Mall and Memorial Parks</option>
# <option>National Park of American Samoa</option>
# <option>National Parks of New York Harbor</option>
# <option>Natural Bridges National Monument</option>
# <option>Navajo National Monument</option>
# <option>New Bedford Whaling National Historical Park</option>
# <option>New England National Scenic Trail</option>
# <option>New Jersey Pinelands National Reserve</option>
# <option>New Orleans Jazz National Historical Park</option>
# <option>New River Gorge National River</option>
# <option>Nez Perce National Historical Park</option>
# <option>Niagara Falls National Heritage Area</option>
# <option>Nicodemus National Historic Site</option>
# <option>Ninety Six National Historic Site</option>
# <option>Niobrara National Scenic River</option>
# <option>Noatak National Preserve</option>
# <option>North Cascades National Park</option>
# <option>North Country National Scenic Trail</option>
# <option>Obed Wild & Scenic River</option>
# <option>Ocmulgee Mounds National Historical Park</option>
# <option>Oil Region National Heritage Area</option>
# <option>Oklahoma City National Memorial</option>
# <option>Old Spanish National Historic Trail</option>
# <option>Olympic National Park</option>
# <option>Oregon Caves National Monument & Preserve</option>
# <option>Oregon National Historic Trail</option>
# <option>Organ Pipe Cactus National Monument</option>
# <option>Overmountain Victory National Historic Trail</option>
# <option>Oxon Cove  Park & Oxon Hill Farm</option>
# <option>Ozark National Scenic Riverways</option>
# <option>Padre Island National Seashore</option>
# <option>Palo Alto Battlefield National Historical Park</option>
# <option>Parashant National Monument</option>
# <option>Paterson Great Falls National Historical Park</option>
# <option>Pea Ridge National Military Park</option>
# <option>Pearl Harbor National Memorial</option>
# <option>Pecos National Historical Park</option>
# <option>Pennsylvania Avenue</option>
# <option>Perry's Victory & International Peace Memorial</option>
# <option>Petersburg National Battlefield</option>
# <option>Petrified Forest National Park</option>
# <option>Petroglyph National Monument</option>
# <option>Pictured Rocks National Lakeshore</option>
# <option>Pinnacles National Park</option>
# <option>Pipe Spring National Monument</option>
# <option>Pipestone National Monument</option>
# <option>Piscataway Park</option>
# <option>Point Reyes National Seashore</option>
# <option>Pony Express National Historic Trail</option>
# <option>Port Chicago Naval Magazine National Memorial</option>
# <option>Potomac Heritage National Scenic Trail</option>
# <option>Poverty Point National Monument</option>
# <option>President William Jefferson Clinton Birthplace Home National Historic Site</option>
# <option>President's Park (White House)</option>
# <option>Presidio of San Francisco</option>
# <option>Prince William Forest Park</option>
# <option>Pu`uhonua O H&#333;naunau National Historical Park</option>
# <option>Pu`ukohol&#257; Heiau National Historic Site</option>
# <option>Pullman National Monument</option>
# <option>Rainbow Bridge National Monument</option>
# <option>Reconstruction Era National Historical Park</option>
# <option>Redwood National and State Parks</option>
# <option>Richmond National Battlefield Park</option>
# <option>Rio Grande Wild & Scenic River</option>
# <option>River Raisin National Battlefield Park</option>
# <option>Rivers Of Steel National Heritage Area</option>
# <option>Rock Creek Park</option>
# <option>Rocky Mountain National Park</option>
# <option>Roger Williams National Memorial</option>
# <option>Roosevelt Campobello International Park</option>
# <option>Rosie the Riveter WWII Home Front National Historical Park</option>
# <option>Russell Cave National Monument</option>
# <option>Sagamore Hill National Historic Site</option>
# <option>Saguaro National Park</option>
# <option>Saint Croix Island International Historic Site</option>
# <option>Saint Croix National Scenic Riverway</option>
# <option>Saint Paul's Church National Historic Site</option>
# <option>Saint-Gaudens National Historical Park</option>
# <option>Salem Maritime National Historic Site</option>
# <option>Salinas Pueblo Missions National Monument</option>
# <option>Salt River Bay National Historical Park and Ecological Preserve</option>
# <option>San Antonio Missions National Historical Park</option>
# <option>San Francisco Maritime National Historical Park</option>
# <option>San Juan Island National Historical Park</option>
# <option>San Juan National Historic Site</option>
# <option>Sand Creek Massacre National Historic Site</option>
# <option>Santa Fe National Historic Trail</option>
# <option>Santa Monica Mountains National Recreation Area</option>
# <option>Saratoga National Historical Park</option>
# <option>Saugus Iron Works National Historic Site</option>
# <option>Schuylkill River Valley National Heritage Area</option>
# <option>Scotts Bluff National Monument</option>
# <option>Selma To Montgomery National Historic Trail</option>
# <option>Sequoia & Kings Canyon National Parks</option>
# <option>Shenandoah National Park</option>
# <option>Shenandoah Valley Battlefields National Historic District</option>
# <option>Shiloh National Military Park</option>
# <option>Sitka National Historical Park</option>
# <option>Sleeping Bear Dunes National Lakeshore</option>
# <option>South Carolina National Heritage Corridor</option>
# <option>Springfield Armory National Historic Site</option>
# <option>Star-Spangled Banner National Historic Trail</option>
# <option>Statue Of Liberty National Monument</option>
# <option>Steamtown National Historic Site</option>
# <option>Stones River National Battlefield</option>
# <option>Stonewall National Monument</option>
# <option>Sunset Crater Volcano National Monument</option>
# <option>Tallgrass Prairie National Preserve</option>
# <option>Tennessee Civil War National Heritage Area</option>
# <option>Thaddeus Kosciuszko National Memorial</option>
# <option>The Last Green Valley National Heritage Corridor</option>
# <option>Theodore Roosevelt Birthplace National Historic Site</option>
# <option>Theodore Roosevelt Inaugural National Historic Site</option>
# <option>Theodore Roosevelt Island</option>
# <option>Theodore Roosevelt National Park</option>
# <option>Thomas Cole National Historic Site</option>
# <option>Thomas Edison National Historical Park</option>
# <option>Thomas Jefferson Memorial</option>
# <option>Thomas Stone National Historic Site</option>
# <option>Timpanogos Cave National Monument</option>
# <option>Timucuan Ecological & Historic Preserve</option>
# <option>Tonto National Monument</option>
# <option>Touro Synagogue National Historic Site</option>
# <option>Trail Of Tears National Historic Trail</option>
# <option>Tule Lake National Monument</option>
# <option>Tule Springs Fossil Beds National Monument</option>
# <option>Tumacácori National Historical Park</option>
# <option>Tupelo National Battlefield</option>
# <option>Tuskegee Airmen National Historic Site</option>
# <option>Tuskegee Institute National Historic Site</option>
# <option>Tuzigoot National Monument</option>
# <option>Ulysses S Grant National Historic Site</option>
# <option>Upper Delaware Scenic & Recreational River</option>
# <option>Valles Caldera National Preserve</option>
# <option>Valley Forge National Historical Park</option>
# <option>Vanderbilt Mansion National Historic Site</option>
# <option>Vicksburg National Military Park</option>
# <option>Vietnam Veterans Memorial</option>
# <option>Virgin Islands Coral Reef National Monument</option>
# <option>Virgin Islands National Park</option>
# <option>Voyageurs National Park</option>
# <option>Waco Mammoth National Monument</option>
# <option>Walnut Canyon National Monument</option>
# <option>War In The Pacific National Historical Park</option>
# <option>Washington Monument</option>
# <option>Washington-Rochambeau National Historic Trail</option>
# <option>Washita Battlefield National Historic Site</option>
# <option>Weir Farm National Historic Site</option>
# <option>Wheeling National Heritage Area</option>
# <option>Whiskeytown National Recreation Area</option>
# <option>White Sands National Monument</option>
# <option>Whitman Mission National Historic Site</option>
# <option>William Howard Taft National Historic Site</option>
# <option>Wilson's Creek National Battlefield</option>
# <option>Wind Cave National Park</option>
# <option>Wing Luke Museum Affiliated Area</option>
# <option>Wolf Trap National Park for the Performing Arts</option>
# <option>Women's Rights National Historical Park</option>
# <option>World War II Memorial</option>
# <option>Wrangell - St Elias National Park & Preserve</option>
# <option>Wright Brothers National Memorial</option>
# <option>Wupatki National Monument</option>
# <option>Yellowstone National Park</option>
# <option>Yorktown Battlefield Part of Colonial National Historical Park</option>
# <option>Yosemite National Park</option>
# <option>Yucca House National Monument</option>
# <option>Yukon - Charley Rivers National Preserve</option>
# <option>Zion National Park</option>



############
# park codes
############

# abli
# acad
# adam
# afam
# afbg
# agfo
# alka
# alag
# anch
# alca
# aleu
# alfl
# alpo
# amme
# amis
# anac
# ande
# anjo
# ania
# anti
# apis
# appa
# apco
# armo
# arch
# arpo
# arho
# asis
# attr
# auca
# azru
# badl
# balt
# bawa
# band
# bepa
# beol
# bela
# bibe
# bicy
# biho
# biso
# bith
# bica
# bicr
# bisc
# blca
# blrv
# blrn
# blri
# blue
# bowa
# boaf
# boha
# bost
# brcr
# brvb
# brca
# buis
# buff
# cabr
# cali
# cane
# cana
# cari
# crha
# cach
# cany
# caco
# caha
# came
# cakr
# calo
# cahi
# care
# cajo
# cavo
# carl
# cave
# cawo
# cagr
# casa
# cacl
# camo
# cato
# cebr
# cebe
# cech
# chcu
# cham
# chva
# chis
# chpi
# chyo
# chat
# choh
# cbpo
# cbgn
# chch
# chic
# chir
# chri
# ciro
# cwdw
# clba
# coal
# colo
# colm
# colt
# cong
# coga
# coro
# cowp
# crla
# crmo
# xrds
# cuga
# cuis
# cure
# cuva
# dabe
# daav
# deso
# deva
# dele
# dewa
# dena
# depo
# deto
# dino
# drto
# ebla
# edal
# efmo
# eise
# elte
# elca
# elma
# elmo
# elro
# elis
# erie
# esse
# euon
# ever
# fati
# feha
# fiis
# fila
# frst
# flni
# flfo
# foth
# fobo
# foda
# fodo
# fodu
# fofo
# fofr
# fola
# fols
# foma
# fomc
# fomr
# fone
# fopo
# fopu
# fora
# fosc
# fosm
# fost
# fosu
# foun
# fous
# fova
# fowa
# fobu
# frde
# frdo
# frla
# frsp
# frri
# frhi
# gaar
# jeff
# gate
# gari
# gegr
# gero
# gewa
# gwca
# gwmp
# gett
# gicl
# glba
# glac
# glca
# glec
# glde
# goga
# gosp
# gois
# grca
# grpo
# grte
# grko
# grba
# greg
# grfa
# grsa
# grsm
# grsp
# gree
# gumo
# guco
# guis
# guge
# hafo
# hale
# hagr
# hamp
# haha
# hafe
# hart
# hatu
# hstr
# havo
# heho
# jame
# pima
# hofr
# home
# hono
# hocu
# hofu
# hobe
# hosp
# hove
# hutr
# hurv
# inup
# iafl
# iatr
# inde
# indu
# isro
# jaga
# jela
# jeca
# jica
# joda
# jofi
# blac
# jomu
# jofl
# jotr
# jthg
# juba
# kala
# kaho
# kaww
# katm
# kefj
# keaq
# kemo
# kewe
# kimo
# klse
# klgo
# knri
# kova
# kowa
# lacl
# lake
# lamr
# laro
# lavo
# labe
# lyba
# lecl
# lewi
# libo
# liho
# linc
# libi
# liri
# chsc
# long
# lowe
# lode
# loea
# lyjo
# mawa
# maac
# maca
# mana
# mapr
# manz
# mabi
# mlkm
# malu
# mava
# mamc
# meve
# miin
# mima
# mimi
# mide
# migu
# mihi
# miss
# mnrr
# moja
# mono
# moca
# mocr
# mopi
# morr
# auto
# mora
# moru
# muwo
# mush
# natc
# natt
# natr
# avia
# nace
# nama
# npsa
# npnh
# nabr
# nava
# nebe
# neen
# pine
# jazz
# neri
# nepe
# nifa
# nico
# nisi
# niob
# noat
# noca
# noco
# obed
# ocmu
# oire
# okci
# olsp
# olym
# orca
# oreg
# orpi
# ovvi
# oxhi
# ozar
# pais
# paal
# para
# pagr
# peri
# valr
# peco
# paav
# pevi
# pete
# pefo
# petr
# piro
# pinn
# pisp
# pipe
# pisc
# pore
# poex
# poch
# pohe
# popo
# wicl
# whho
# prsf
# prwi
# puho
# puhe
# pull
# rabr
# reer
# redw
# rich
# rigr
# rira
# rist
# rocr
# romo
# rowi
# roca
# rori
# ruca
# sahi
# sagu
# sacr
# sacn
# sapa
# saga
# sama
# sapu
# sari
# saan
# safr
# sajh
# saju
# sand
# safe
# samo
# sara
# sair
# scrv
# scbl
# semo
# seki
# shen
# shvb
# shil
# sitk
# slbe
# soca
# spar
# stsp
# stli
# stea
# stri
# ston
# sucr
# tapr
# tecw
# thko
# qush
# thrb
# thri
# this
# thro
# thco
# edis
# thje
# thst
# tica
# timu
# tont
# tosy
# trte
# tule
# tusk
# tuma
# tupe
# tuai
# tuin
# tuzi
# ulsg
# upde
# vall
# vafo
# vama
# vick
# vive
# vicr
# viis
# voya
# waco
# waca
# wapa
# wamo
# waro
# waba
# wefa
# whee
# whis
# whsa
# whmi
# wiho
# wicr
# wica
# wing
# wotr
# wori
# wwii
# wrst
# wrbr
# wupa
# yell
# york
# yose
# yuho
# yuch
# zion


##########################
# park name with park code
##########################

# Abraham Lincoln Birthplace National Historical Park, abli
# Acadia National Park, acad
# Adams National Historical Park, adam
# African American Civil War Memorial, afam
# African Burial Ground National Monument, afbg
# Agate Fossil Beds National Monument, agfo
# Ala Kahakai National Historic Trail, alka
# Alagnak Wild River, alag
# Alaska Public Lands, anch
# Alcatraz Island, alca
# Aleutian Islands World War II National Historic Area, aleu
# Alibates Flint Quarries National Monument, alfl
# Allegheny Portage Railroad National Historic Site, alpo
# American Memorial Park, amme
# Amistad National Recreation Area, amis
# Anacostia Park, anac
# Andersonville National Historic Site, ande
# Andrew Johnson National Historic Site, anjo
# Aniakchak National Monument & Preserve, ania
# Antietam National Battlefield, anti
# Apostle Islands National Lakeshore, apis
# Appalachian National Scenic Trail, appa
# Appomattox Court House National Historical Park, apco
# Arabia Mountain National Heritage Area, armo
# Arches National Park, arch
# Arkansas Post National Memorial, arpo
# Arlington House, The Robert  E. Lee Memorial, arho
# Assateague Island National Seashore, asis
# Atchafalaya National Heritage Area, attr
# Augusta Canal National Heritage Area, auca
# Aztec Ruins National Monument, azru
# Badlands National Park, badl
# Baltimore National Heritage Area, balt
# Baltimore-Washington Parkway, bawa
# Bandelier National Monument, band
# Belmont-Paul Women's Equality National Monument, bepa
# Bent's Old Fort National Historic Site, beol
# Bering Land Bridge National Preserve, bela
# Big Bend National Park, bibe
# Big Cypress National Preserve, bicy
# Big Hole National Battlefield, biho
# Big South Fork National River & Recreation Area, biso
# Big Thicket National Preserve, bith
# Bighorn Canyon National Recreation Area, bica
# Birmingham Civil Rights National Monument, bicr
# Biscayne National Park, bisc
# Black Canyon Of The Gunnison National Park, blca
# Blackstone River Valley National Historical Park, blrv
# Blue Ridge National Heritage Area, blrn
# Blue Ridge Parkway, blri
# Bluestone National Scenic River, blue
# Booker T Washington National Monument, bowa
# Boston African American National Historic Site, boaf
# Boston Harbor Islands National Recreation Area, boha
# Boston National Historical Park, bost
# Brices Cross Roads National Battlefield Site, brcr
# Brown v. Board of Education National Historic Site, brvb
# Bryce Canyon National Park, brca
# Buck Island Reef National Monument, buis
# Buffalo National River, buff
# Cabrillo National Monument, cabr
# California National Historic Trail, cali
# Camp Nelson National Monument, cane
# Canaveral National Seashore, cana
# Cane River Creole National Historical Park, cari
# Cane River National Heritage Area, crha
# Canyon de Chelly National Monument, cach
# Canyonlands National Park, cany
# Cape Cod National Seashore, caco
# Cape Hatteras National Seashore, caha
# Cape Henry Memorial Part of Colonial National Historical Park, came
# Cape Krusenstern National Monument, cakr
# Cape Lookout National Seashore, calo
# Capitol Hill Parks, cahi
# Capitol Reef National Park, care
# Captain John Smith Chesapeake National Historic Trail, cajo
# Capulin Volcano National Monument, cavo
# Carl Sandburg Home National Historic Site, carl
# Carlsbad Caverns National Park, cave
# Carter G. Woodson Home National Historic Site, cawo
# Casa Grande Ruins National Monument, cagr
# Castillo de San Marcos National Monument, casa
# Castle Clinton National Monument, cacl
# Castle Mountains National Monument, camo
# Catoctin Mountain Park, cato
# Cedar Breaks National Monument, cebr
# Cedar Creek & Belle Grove National Historical Park, cebe
# César E. Chávez National Monument, cech
# Chaco Culture National Historical Park, chcu
# Chamizal National Memorial, cham
# Champlain Valley National Heritage Partnership, chva
# Channel Islands National Park, chis
# Charles Pinckney National Historic Site, chpi
# Charles Young Buffalo Soldiers National Monument, chyo
# Chattahoochee River National Recreation Area, chat
# Chesapeake & Ohio Canal National Historical Park, choh
# Chesapeake Bay, cbpo
# Chesapeake Bay Gateways and Watertrails Network, cbgn
# Chickamauga & Chattanooga National Military Park, chch
# Chickasaw National Recreation Area, chic
# Chiricahua National Monument, chir
# Christiansted National Historic Site, chri
# City Of Rocks National Reserve, ciro
# Civil War Defenses of Washington, cwdw
# Clara Barton National Historic Site, clba
# Coal National Heritage Area, coal
# Colonial National Historical Park, colo
# Colorado National Monument, colm
# Coltsville National Historical Park, colt
# Congaree National Park, cong
# Constitution Gardens, coga
# Coronado National Memorial, coro
# Cowpens National Battlefield, cowp
# Crater Lake National Park, crla
# Craters Of The Moon National Monument & Preserve, crmo
# Crossroads of the American Revolution National Heritage Area, xrds
# Cumberland Gap National Historical Park, cuga
# Cumberland Island National Seashore, cuis
# Curecanti National Recreation Area, cure
# Cuyahoga Valley National Park, cuva
# David Berger National Memorial, dabe
# Dayton Aviation Heritage National Historical Park, daav
# De Soto National Memorial, deso
# Death Valley National Park, deva
# Delaware & Lehigh National Heritage Corridor, dele
# Delaware Water Gap National Recreation Area, dewa
# Denali National Park & Preserve, dena
# Devils Postpile National Monument, depo
# Devils Tower National Monument, deto
# Dinosaur National Monument, dino
# Dry Tortugas National Park, drto
# Ebey's Landing National Historical Reserve, ebla
# Edgar Allan Poe National Historic Site, edal
# Effigy Mounds National Monument, efmo
# Eisenhower National Historic Site, eise
# El Camino Real de los Tejas National Historic Trail, elte
# El Camino Real de Tierra Adentro National Historic Trail, elca
# El Malpais National Monument, elma
# El Morro National Monument, elmo
# Eleanor Roosevelt National Historic Site, elro
# Ellis Island Part of Statue of Liberty National Monument, elis
# Erie Canalway National Heritage Corridor, erie
# Essex National Heritage Area, esse
# Eugene O'Neill National Historic Site, euon
# Everglades National Park, ever
# Fallen Timbers Battlefield and Fort Miamis National Historic Site, fati
# Federal Hall National Memorial, feha
# Fire Island National Seashore, fiis
# First Ladies National Historic Site, fila
# First State National Historical Park, frst
# Flight 93 National Memorial, flni
# Florissant Fossil Beds National Monument, flfo
# Ford's Theatre, foth
# Fort Bowie National Historic Site, fobo
# Fort Davis National Historic Site, foda
# Fort Donelson National Battlefield, fodo
# Fort Dupont Park, fodu
# Fort Foote Park, fofo
# Fort Frederica National Monument, fofr
# Fort Laramie National Historic Site, fola
# Fort Larned National Historic Site, fols
# Fort Matanzas National Monument, foma
# Fort McHenry National Monument and Historic Shrine, fomc
# Fort Monroe National Monument, fomr
# Fort Necessity National Battlefield, fone
# Fort Point National Historic Site, fopo
# Fort Pulaski National Monument, fopu
# Fort Raleigh National Historic Site, fora
# Fort Scott National Historic Site, fosc
# Fort Smith National Historic Site, fosm
# Fort Stanwix National Monument, fost
# Fort Sumter and Fort Moultrie National Historical Park, fosu
# Fort Union National Monument, foun
# Fort Union Trading Post National Historic Site, fous
# Fort Vancouver National Historic Site, fova
# Fort Washington Park, fowa
# Fossil Butte National Monument, fobu
# Franklin Delano Roosevelt Memorial, frde
# Frederick Douglass National Historic Site, frdo
# Frederick Law Olmsted National Historic Site, frla
# Fredericksburg & Spotsylvania National Military Park, frsp
# Freedom Riders National Monument, frri
# Friendship Hill National Historic Site, frhi
# Gates Of The Arctic National Park & Preserve, gaar
# Gateway Arch National Park, jeff
# Gateway National Recreation Area, gate
# Gauley River National Recreation Area, gari
# General Grant National Memorial, gegr
# George Rogers Clark National Historical Park, gero
# George Washington Birthplace National Monument, gewa
# George Washington Carver National Monument, gwca
# George Washington Memorial Parkway, gwmp
# Gettysburg National Military Park, gett
# Gila Cliff Dwellings National Monument, gicl
# Glacier Bay National Park & Preserve, glba
# Glacier National Park, glac
# Glen Canyon National Recreation Area, glca
# Glen Echo Park, glec
# Gloria Dei Church National Historic Site, glde
# Golden Gate National Recreation Area, goga
# Golden Spike National Historical Park, gosp
# Governors Island National Monument, gois
# Grand Canyon National Park, grca
# Grand Portage National Monument, grpo
# Grand Teton National Park, grte
# Grant-Kohrs Ranch National Historic Site, grko
# Great Basin National Park, grba
# Great Egg Harbor River, greg
# Great Falls Park, grfa
# Great Sand Dunes National Park & Preserve, grsa
# Great Smoky Mountains National Park, grsm
# Green Springs, grsp
# Greenbelt Park, gree
# Guadalupe Mountains National Park, gumo
# Guilford Courthouse National Military Park, guco
# Gulf Islands National Seashore, guis
# Gullah/Geechee Cultural Heritage Corridor, guge
# Hagerman Fossil Beds National Monument, hafo
# Haleakal&#257; National Park, hale
# Hamilton Grange National Memorial, hagr
# Hampton National Historic Site, hamp
# Harmony Hall, haha
# Harpers Ferry National Historical Park, hafe
# Harriet Tubman National Historical Park, hart
# Harriet Tubman Underground Railroad National Historical Park, hatu
# Harry S Truman National Historic Site, hstr
# Hawai'i Volcanoes National Park, havo
# Herbert Hoover National Historic Site, heho
# Historic Jamestowne Part of Colonial National Historical Park, jame
# Hohokam Pima National Monument, pima
# Home Of Franklin D Roosevelt National Historic Site, hofr
# Homestead National Monument of America, home
# Honouliuli National Historic Site, hono
# Hopewell Culture National Historical Park, hocu
# Hopewell Furnace National Historic Site, hofu
# Horseshoe Bend National Military Park, hobe
# Hot Springs National Park, hosp
# Hovenweep National Monument, hove
# Hubbell Trading Post National Historic Site, hutr
# Hudson River Valley National Heritage Area, hurv
# I&#241;upiat Heritage Center, inup
# Ice Age Floods National Geologic Trail, iafl
# Ice Age National Scenic Trail, iatr
# Independence National Historical Park, inde
# Indiana Dunes National Park, indu
# Isle Royale National Park, isro
# James A Garfield National Historic Site, jaga
# Jean Lafitte National Historical Park and Preserve, jela
# Jewel Cave National Monument, jeca
# Jimmy Carter National Historic Site, jica
# John Day Fossil Beds National Monument, joda
# John Fitzgerald Kennedy National Historic Site, jofi
# John H. Chafee Blackstone River Valley National Heritage Corridor, blac
# John Muir National Historic Site, jomu
# Johnstown Flood National Memorial, jofl
# Joshua Tree National Park, jotr
# Journey Through Hallowed Ground National Heritage Area, jthg
# Juan Bautista de Anza National Historic Trail, juba
# Kalaupapa National Historical Park, kala
# Kaloko-Honok&#333;hau National Historical Park, kaho
# Katahdin Woods and Waters National Monument, kaww
# Katmai National Park & Preserve, katm
# Kenai Fjords National Park, kefj
# Kenilworth Park & Aquatic Gardens, keaq
# Kennesaw Mountain National Battlefield Park, kemo
# Keweenaw National Historical Park, kewe
# Kings Mountain National Military Park, kimo
# Klondike Gold Rush - Seattle Unit National Historical Park, klse
# Klondike Gold Rush National Historical Park, klgo
# Knife River Indian Villages National Historic Site, knri
# Kobuk Valley National Park, kova
# Korean War Veterans Memorial, kowa
# Lake Clark National Park & Preserve, lacl
# Lake Mead National Recreation Area, lake
# Lake Meredith National Recreation Area, lamr
# Lake Roosevelt National Recreation Area, laro
# Lassen Volcanic National Park, lavo
# Lava Beds National Monument, labe
# LBJ Memorial Grove on the Potomac, lyba
# Lewis & Clark National Historic Trail, lecl
# Lewis and Clark National Historical Park, lewi
# Lincoln Boyhood National Memorial, libo
# Lincoln Home National Historic Site, liho
# Lincoln Memorial, linc
# Little Bighorn Battlefield National Monument, libi
# Little River Canyon National Preserve, liri
# Little Rock Central High School National Historic Site, chsc
# Longfellow House Washington's Headquarters National Historic Site, long
# Lowell National Historical Park, lowe
# Lower Delaware National Wild and Scenic River, lode
# Lower East Side Tenement Museum National Historic Site, loea
# Lyndon B Johnson National Historical Park, lyjo
# Maggie L Walker National Historic Site, mawa
# Maine Acadian Culture, maac
# Mammoth Cave National Park, maca
# Manassas National Battlefield Park, mana
# Manhattan Project National Historical Park, mapr
# Manzanar National Historic Site, manz
# Marsh - Billings - Rockefeller National Historical Park, mabi
# Martin Luther King, Jr. Memorial, mlkm
# Martin Luther King, Jr. National Historical Park, malu
# Martin Van Buren National Historic Site, mava
# Mary McLeod Bethune Council House National Historic Site, mamc
# Mesa Verde National Park, meve
# Minidoka National Historic Site, miin
# Minute Man National Historical Park, mima
# Minuteman Missile National Historic Site, mimi
# Mississippi Delta National Heritage Area, mide
# Mississippi Gulf National Heritage Area, migu
# Mississippi Hills National Heritage Area, mihi
# Mississippi National River and Recreation Area, miss
# Missouri National Recreational River, mnrr
# Mojave National Preserve, moja
# Monocacy National Battlefield, mono
# Montezuma Castle National Monument, moca
# Moores Creek National Battlefield, mocr
# Mormon Pioneer National Historic Trail, mopi
# Morristown National Historical Park, morr
# Motor Cities National Heritage Area, auto
# Mount Rainier National Park, mora
# Mount Rushmore National Memorial, moru
# Muir Woods National Monument, muwo
# Muscle Shoals National Heritage Area, mush
# Natchez National Historical Park, natc
# Natchez Trace National Scenic Trail, natt
# Natchez Trace Parkway, natr
# National Aviation Heritage Area, avia
# National Capital Parks-East, nace
# National Mall and Memorial Parks, nama
# National Park of American Samoa, npsa
# National Parks of New York Harbor, npnh
# Natural Bridges National Monument, nabr
# Navajo National Monument, nava
# New Bedford Whaling National Historical Park, nebe
# New England National Scenic Trail, neen
# New Jersey Pinelands National Reserve, pine
# New Orleans Jazz National Historical Park, jazz
# New River Gorge National River, neri
# Nez Perce National Historical Park, nepe
# Niagara Falls National Heritage Area, nifa
# Nicodemus National Historic Site, nico
# Ninety Six National Historic Site, nisi
# Niobrara National Scenic River, niob
# Noatak National Preserve, noat
# North Cascades National Park, noca
# North Country National Scenic Trail, noco
# Obed Wild & Scenic River, obed
# Ocmulgee Mounds National Historical Park, ocmu
# Oil Region National Heritage Area, oire
# Oklahoma City National Memorial, okci
# Old Spanish National Historic Trail, olsp
# Olympic National Park, olym
# Oregon Caves National Monument & Preserve, orca
# Oregon National Historic Trail, oreg
# Organ Pipe Cactus National Monument, orpi
# Overmountain Victory National Historic Trail, ovvi
# Oxon Cove  Park & Oxon Hill Farm, oxhi
# Ozark National Scenic Riverways, ozar
# Padre Island National Seashore, pais
# Palo Alto Battlefield National Historical Park, paal
# Parashant National Monument, para
# Paterson Great Falls National Historical Park, pagr
# Pea Ridge National Military Park, peri
# Pearl Harbor National Memorial, valr
# Pecos National Historical Park, peco
# Pennsylvania Avenue, paav
# Perry's Victory & International Peace Memorial, pevi
# Petersburg National Battlefield, pete
# Petrified Forest National Park, pefo
# Petroglyph National Monument, petr
# Pictured Rocks National Lakeshore, piro
# Pinnacles National Park, pinn
# Pipe Spring National Monument, pisp
# Pipestone National Monument, pipe
# Piscataway Park, pisc
# Point Reyes National Seashore, pore
# Pony Express National Historic Trail, poex
# Port Chicago Naval Magazine National Memorial, poch
# Potomac Heritage National Scenic Trail, pohe
# Poverty Point National Monument, popo
# President William Jefferson Clinton Birthplace Home National Historic Site, wicl
# President's Park (White House), whho
# Presidio of San Francisco, prsf
# Prince William Forest Park, prwi
# Pu`uhonua O H&#333;naunau National Historical Park, puho
# Pu`ukohol&#257; Heiau National Historic Site, puhe
# Pullman National Monument, pull
# Rainbow Bridge National Monument, rabr
# Reconstruction Era National Historical Park, reer
# Redwood National and State Parks, redw
# Richmond National Battlefield Park, rich
# Rio Grande Wild & Scenic River, rigr
# River Raisin National Battlefield Park, rira
# Rivers Of Steel National Heritage Area, rist
# Rock Creek Park, rocr
# Rocky Mountain National Park, romo
# Roger Williams National Memorial, rowi
# Roosevelt Campobello International Park, roca
# Rosie the Riveter WWII Home Front National Historical Park, rori
# Russell Cave National Monument, ruca
# Sagamore Hill National Historic Site, sahi
# Saguaro National Park, sagu
# Saint Croix Island International Historic Site, sacr
# Saint Croix National Scenic Riverway, sacn
# Saint Paul's Church National Historic Site, sapa
# Saint-Gaudens National Historical Park, saga
# Salem Maritime National Historic Site, sama
# Salinas Pueblo Missions National Monument, sapu
# Salt River Bay National Historical Park and Ecological Preserve, sari
# San Antonio Missions National Historical Park, saan
# San Francisco Maritime National Historical Park, safr
# San Juan Island National Historical Park, sajh
# San Juan National Historic Site, saju
# Sand Creek Massacre National Historic Site, sand
# Santa Fe National Historic Trail, safe
# Santa Monica Mountains National Recreation Area, samo
# Saratoga National Historical Park, sara
# Saugus Iron Works National Historic Site, sair
# Schuylkill River Valley National Heritage Area, scrv
# Scotts Bluff National Monument, scbl
# Selma To Montgomery National Historic Trail, semo
# Sequoia & Kings Canyon National Parks, seki
# Shenandoah National Park, shen
# Shenandoah Valley Battlefields National Historic District, shvb
# Shiloh National Military Park, shil
# Sitka National Historical Park, sitk
# Sleeping Bear Dunes National Lakeshore, slbe
# South Carolina National Heritage Corridor, soca
# Springfield Armory National Historic Site, spar
# Star-Spangled Banner National Historic Trail, stsp
# Statue Of Liberty National Monument, stli
# Steamtown National Historic Site, stea
# Stones River National Battlefield, stri
# Stonewall National Monument, ston
# Sunset Crater Volcano National Monument, sucr
# Tallgrass Prairie National Preserve, tapr
# Tennessee Civil War National Heritage Area, tecw
# Thaddeus Kosciuszko National Memorial, thko
# The Last Green Valley National Heritage Corridor, qush
# Theodore Roosevelt Birthplace National Historic Site, thrb
# Theodore Roosevelt Inaugural National Historic Site, thri
# Theodore Roosevelt Island, this
# Theodore Roosevelt National Park, thro
# Thomas Cole National Historic Site, thco
# Thomas Edison National Historical Park, edis
# Thomas Jefferson Memorial, thje
# Thomas Stone National Historic Site, thst
# Timpanogos Cave National Monument, tica
# Timucuan Ecological & Historic Preserve, timu
# Tonto National Monument, tont
# Touro Synagogue National Historic Site, tosy
# Trail Of Tears National Historic Trail, trte
# Tule Lake National Monument, tule
# Tule Springs Fossil Beds National Monument, tusk
# Tumacácori National Historical Park, tuma
# Tupelo National Battlefield, tupe
# Tuskegee Airmen National Historic Site, tuai
# Tuskegee Institute National Historic Site, tuin
# Tuzigoot National Monument, tuzi
# Ulysses S Grant National Historic Site, ulsg
# Upper Delaware Scenic & Recreational River, upde
# Valles Caldera National Preserve, vall
# Valley Forge National Historical Park, vafo
# Vanderbilt Mansion National Historic Site, vama
# Vicksburg National Military Park, vick
# Vietnam Veterans Memorial, vive
# Virgin Islands Coral Reef National Monument, vicr
# Virgin Islands National Park, viis
# Voyageurs National Park, voya
# Waco Mammoth National Monument, waco
# Walnut Canyon National Monument, waca
# War In The Pacific National Historical Park, wapa
# Washington Monument, wamo
# Washington-Rochambeau National Historic Trail, waro
# Washita Battlefield National Historic Site, waba
# Weir Farm National Historic Site, wefa
# Wheeling National Heritage Area, whee
# Whiskeytown National Recreation Area, whis
# White Sands National Monument, whsa
# Whitman Mission National Historic Site, whmi
# William Howard Taft National Historic Site, wiho
# Wilson's Creek National Battlefield, wicr
# Wind Cave National Park, wica
# Wing Luke Museum Affiliated Area, wing
# Wolf Trap National Park for the Performing Arts, wotr
# Women's Rights National Historical Park, wori
# World War II Memorial, wwii
# Wrangell - St Elias National Park & Preserve, wrst
# Wright Brothers National Memorial, wrbr
# Wupatki National Monument, wupa
# Yellowstone National Park, yell
# Yorktown Battlefield Part of Colonial National Historical Park, york
# Yosemite National Park, yose
# Yucca House National Monument, yuho
# Yukon - Charley Rivers National Preserve, yuch
# Zion National Park, zion


#########
# states 
########


# KY
# ME
# MA
# DC
# NY
# NE
# HI
# AK
# AK
# CA
# AK
# TX
# PA
# MP
# TX
# DC
# GA
# TN
# AK
# MD
# WI
# CT,GA,MA,MD,ME,NC,NH,NJ,NY,PA,TN,VA,VT,WV
# VA
# GA
# UT
# AR
# VA
# MD,VA
# LA
# GA
# NM
# SD
# MD
# MD
# NM
# DC
# CO
# AK
# TX
# FL
# MT
# KY,TN
# TX
# MT,WY
# AL
# FL
# CO
# RI,MA
# NC
# NC,VA
# WV
# VA
# MA
# MA
# MA
# MS
# KS
# UT
# VI
# AR
# CA
# CA,CO,ID,KS,MO,NE,NV,OR,UT,WY
# KY
# FL
# LA
# LA
# AZ
# UT
# MA
# NC
# VA
# AK
# NC
# DC
# UT
# VA,MD,DE,DC,PA,NY
# NM
# NC
# NM
# DC
# AZ
# FL
# NY
# CA
# MD
# UT
# VA
# CA
# NM
# TX
# VT,NY
# CA
# SC
# OH
# GA
# DC,MD,WV
# DC,DE,MD,NY,PA,VA,WV
# DC,MD,NY,PA,VA,WV
# GA,TN
# OK
# AZ
# VI
# ID
# DC,MD,VA
# MD
# WV
# VA
# CO
# CT
# SC
# DC
# AZ
# SC
# OR
# ID
# NJ
# KY,TN,VA
# GA
# CO
# OH
# OH
# OH
# FL
# CA,NV
# PA
# NJ,PA
# AK
# CA
# WY
# CO,UT
# FL
# WA
# PA
# IA
# PA
# TX,LA
# NM,TX
# NM
# NM
# NY
# NJ,NY
# NY
# MA
# CA
# FL
# OH
# NY
# NY
# OH
# DE,PA
# PA
# CO
# DC
# AZ
# TX
# KY,TN
# DC
# MD
# GA
# WY
# KS
# FL
# MD
# VA
# PA
# CA
# GA
# NC
# KS
# AR,OK
# NY
# SC
# NM
# MT,ND
# OR,WA
# MD
# WY
# DC
# DC
# MA
# VA
# AL
# PA
# AK
# MO
# NY,NJ
# WV
# NY
# IN
# VA
# MO
# DC,MD,VA
# PA
# NM
# AK
# MT
# AZ,UT
# MD
# PA
# CA
# UT
# NY
# AZ
# MN
# WY
# MT
# NV
# NJ
# VA
# CO
# NC,TN
# VA
# MD
# TX
# NC
# FL,MS
# FL,GA,NC,SC
# ID
# HI
# NY
# MD
# MD



##############
# designations
##############

# National Historical Park
# National Park
# National Historical Park

# National Monument
# National Monument
# National Historic Trail
# Wild River


# National Historic Area
# National Monument
# National Historic Site
# Park
# National Recreation Area
# Park
# National Historic Site
# National Historic Site
# National Monument & Preserve
# National Battlefield
# National Lakeshore
# National Scenic Trail
# National Historical Park
# National Heritage Area
# National Park
# National Memorial

# National Seashore
# National Heritage Area
# National Heritage Area
# National Monument
# National Park
# National Heritage Area
# Parkway
# National Monument
# National Monument
# National Historic Site
# National Preserve
# National Park
# National Preserve
# National Battlefield
# National River & Recreation Area
# National Preserve
# National Recreation Area
# National Monument
# National Park
# National Park
# National Historical Park
# National Heritage Area
# Parkway
# National Scenic River
# National Monument
# National Historic Site
# National Recreation Area
# National Historical Park
# National Battlefield Site
# National Historic Site
# National Park
# National Monument
# National River
# National Monument
# National Historic Trail
# National Monument
# National Seashore
# National Historical Park
# National Heritage Area
# National Monument
# National Park
# National Seashore
# National Seashore
# Part of Colonial National Historical Park
# National Monument
# National Seashore

# National Park
# National Historic Trail
# National Monument
# National Historic Site
# National Park
# National Historic Site
# National Monument
# National Monument
# National Monument
# National Monument
# Park
# National Monument
# National Historical Park
# National Monument
# National Historical Park
# National Memorial
# National Heritage Partnership
# National Park
# National Historic Site
# National Monument
# National Recreation Area
# National Historical Park


# National Military Park
# National Recreation Area
# National Monument
# National Historic Site
# National Reserve

# National Historic Site
# National Heritage Area
# National Historical Park
# National Monument
# National Historical Park
# National Park

# National Memorial
# National Battlefield
# National Park
# National Monument & Preserve
# National Heritage Area
# National Historical Park
# National Seashore
# National Recreation Area
# National Park
# National Memorial
# National Historical Park
# National Memorial
# National Park
# National Heritage Corridor
# National Recreation Area
# National Park & Preserve
# National Monument
# National Monument
# National Monument
# National Park
# National Historical Reserve
# National Historic Site
# National Monument
# National Historic Site
# National Historic Trail
# National Historic Trail
# National Monument
# National Monument
# National Historic Site
# Part of Statue of Liberty National Monument
# National Heritage Corridor
# National Heritage Area
# National Historic Site
# National Park
# National Historic Site
# National Memorial
# National Seashore
# National Historic Site
# National Historical Park
# National Memorial
# National Monument

# National Historic Site
# National Historic Site
# National Battlefield

# Park
# National Monument
# National Historic Site
# National Historic Site
# National Monument
# National Monument and Historic Shrine
# National Monument
# National Battlefield
# National Historic Site
# National Monument
# National Historic Site
# National Historic Site
# National Historic Site
# National Monument
# National Historical Park
# National Monument
# National Historic Site
# National Historic Site
# Park
# National Monument

# National Historic Site
# National Historic Site
# National Military Park
# National Monument
# National Historic Site
# National Park & Preserve
# National Park
# National Recreation Area
# National Recreation Area
# National Memorial
# National Historical Park
# National Monument
# National Monument
# Memorial Parkway
# National Military Park
# National Monument
# National Park & Preserve
# National Park
# National Recreation Area
# Park
# National Historic Site
# National Recreation Area
# National Historical Park
# National Monument
# National Park
# National Monument
# National Park
# National Historic Site
# National Park

# Park
# National Park & Preserve
# National Park

# Park
# National Park
# National Military Park
# National Seashore
# Cultural Heritage Corridor
# National Monument
# National Park
# National Memorial
# National Historic Site

# National Historical Park
# National Historical Park
# National Historical Park
# National Historic Site
# National Park
# National Historic Site
# Part of Colonial National Historical Park
# National Monument
# National Historic Site
# National Monument of America
# National Historic Site
# National Historical Park
# National Historic Site
# National Military Park
# National Park
# National Monument
# National Historic Site
# National Heritage Area

# National Geologic Trail
# National Scenic Trail
# National Historical Park
# National Park
# National Park
# National Historic Site
# National Historical Park and Preserve
# National Monument
# National Historic Site
# National Monument
# National Historic Site
# National Heritage Corridor
# National Historic Site
# National Memorial
# National Park
# National Heritage Area
# National Historic Trail
# National Historical Park
# National Historical Park
# National Monument
# National Park & Preserve
# National Park

# National Battlefield Park
# National Historical Park
# National Military Park
# National Historical Park
# National Historical Park
# National Historic Site
# National Park

# National Park & Preserve
# National Recreation Area
# National Recreation Area
# National Recreation Area
# National Park
# National Monument

# National Historic Trail
# National Historical Park
# National Memorial
# National Historic Site

# National Monument
# National Preserve
# National Historic Site
# National Historic Site
# National Historical Park
# National Wild and Scenic River
# National Historic Site
# National Historical Park
# National Historic Site

# National Park
# National Battlefield Park
# National Historical Park
# National Historic Site
# National Historical Park

# National Historical Park
# National Historic Site
# National Historic Site
# National Park
# National Historic Site
# National Historical Park
# National Historic Site
# National Heritage Area
# National Heritage Area
# National Heritage Area
# National River and Recreation Area
# National Recreational River
# National Preserve
# National Battlefield
# National Monument
# National Battlefield
# National Historic Trail
# National Historical Park
# National Heritage Area
# National Park
# National Memorial
# National Monument
# National Heritage Area
# National Historical Park
# National Scenic Trail
# Parkway
# Heritage Area




# National Monument
# National Monument
# National Historical Park
# National Scenic Trail
# National Reserve
# National Historical Park
# National River
# National Historical Park
# National Heritage Area
# National Historic Site
# National Historic Site
# National Scenic River
# National Preserve
# National Park
# National Scenic Trail
# Wild & Scenic River
# National Historical Park
# National Heritage Area
# National Memorial
# National Historic Trail
# National Park
# National Monument & Preserve
# National Historic Trail
# National Monument
# National Historic Trail

# National Scenic Riverways
# National Seashore
# National Historical Park
# National Monument
# National Historical Park
# National Military Park
# National Memorial
# National Historical Park

# Memorial
# National Battlefield
# National Park
# National Monument
# National Lakeshore
# National Park
# National Monument
# National Monument
# Park
# National Seashore
# National Historic Trail
# National Memorial
# National Scenic Trail
# National Monument
# National Historic Site


# Park
# National Historical Park
# National Historic Site
# National Monument
# National Monument
# National Historical Park
# National and State Parks
# National Battlefield Park
# Wild & Scenic River
# National Battlefield Park
# National Heritage Area
# Park
# National Park
# National Memorial
# International Park
# National Historical Park
# National Monument
# National Historic Site
# National Park
# International Historic Site
# National Scenic Riverway
# National Historic Site
# National Historical Park
# National Historic Site
# National Monument
# National Historical Park and Ecological Preserve
# National Historical Park
# National Historical Park
# National Historical Park
# National Historic Site
# National Historic Site
# National Historic Trail
# National Recreation Area
# National Historical Park
# National Historic Site
# National Heritage Area
# National Monument
# National Historic Trail
# National Parks
# National Park
# National Historic District
# National Military Park
# National Historical Park
# National Lakeshore
# National Heritage Corridor
# National Historic Site
# National Historic Trail
# National Monument
# National Historic Site
# National Battlefield
# National Monument
# National Monument
# National Preserve
# National Heritage Area
# National Memorial
# National Heritage Corridor
# National Historic Site
# National Historic Site

# National Park
# National Historic Site
# National Historical Park

# National Historic Site
# National Monument
# Ecological & Historic Preserve
# National Monument
# National Historic Site
# National Historic Trail
# National Monument
# National Monument
# National Historical Park
# National Battlefield
# National Historic Site
# National Historic Site
# National Monument
# National Historic Site
# Scenic & Recreational River
# National Preserve
# National Historical Park
# National Historic Site
# National Military Park
# Memorial
# National Monument
# National Park
# National Park
# National Monument
# National Monument
# National Historical Park

# National Historic Trail
# National Historic Site
# National Historic Site
# National Heritage Area
# National Recreation Area
# National Monument
# National Historic Site
# National Historic Site
# National Battlefield
# National Park
# Affiliated Area

# National Historical Park

# National Park & Preserve
# National Memorial
# National Monument
# National Park
# Part of Colonial National Historical Park
# National Park
# National Monument
# National Preserve
# National Park


################
# final appended
################

# Abraham Lincoln Birthplace National Historical Park, abli, National Historical Park, KY
# Acadia National Park, acad, National Park, ME
# Adams National Historical Park, adam, National Historical Park, MA
# African American Civil War Memorial, afam, , DC
# African Burial Ground National Monument, afbg, National Monument, NY
# Agate Fossil Beds National Monument, agfo, National Monument, NE
# Ala Kahakai National Historic Trail, alka, National Historic Trail, HI
# Alagnak Wild River, alag, Wild River, AK
# Alaska Public Lands, anch, , AK
# Alcatraz Island, alca, , CA
# Aleutian Islands World War II National Historic Area, aleu, National Historic Area, AK
# Alibates Flint Quarries National Monument, alfl, National Monument, TX
# Allegheny Portage Railroad National Historic Site, alpo, National Historic Site, PA
# American Memorial Park, amme, Park, MP
# Amistad National Recreation Area, amis, National Recreation Area, TX
# Anacostia Park, anac, Park, DC
# Andersonville National Historic Site, ande, National Historic Site, GA
# Andrew Johnson National Historic Site, anjo, National Historic Site, TN
# Aniakchak National Monument & Preserve, ania, National Monument & Preserve, AK
# Antietam National Battlefield, anti, National Battlefield, MD
# Apostle Islands National Lakeshore, apis, National Lakeshore, WI
# Appalachian National Scenic Trail, appa, National Scenic Trail, CT,GA,MA,MD,ME,NC,NH,NJ,NY,PA,TN,VA,VT,WV
# Appomattox Court House National Historical Park, apco, National Historical Park, VA
# Arabia Mountain National Heritage Area, armo, National Heritage Area, GA
# Arches National Park, arch, National Park, UT
# Arkansas Post National Memorial, arpo, National Memorial, AR
# Arlington House, The Robert  E. Lee Memorial, arho, , VA
# Assateague Island National Seashore, asis, National Seashore, MD,VA
# Atchafalaya National Heritage Area, attr, National Heritage Area, LA
# Augusta Canal National Heritage Area, auca, National Heritage Area, GA
# Aztec Ruins National Monument, azru, National Monument, NM
# Badlands National Park, badl, National Park, SD
# Baltimore National Heritage Area, balt, National Heritage Area, MD
# Baltimore-Washington Parkway, bawa, Parkway, MD
# Bandelier National Monument, band, National Monument, NM
# Belmont-Paul Women's Equality National Monument, bepa, National Monument, DC
# Bent's Old Fort National Historic Site, beol, National Historic Site, CO
# Bering Land Bridge National Preserve, bela, National Preserve, AK
# Big Bend National Park, bibe, National Park, TX
# Big Cypress National Preserve, bicy, National Preserve, FL
# Big Hole National Battlefield, biho, National Battlefield, MT
# Big South Fork National River & Recreation Area, biso, National River & Recreation Area, KY,TN
# Big Thicket National Preserve, bith, National Preserve, TX
# Bighorn Canyon National Recreation Area, bica, National Recreation Area, MT,WY
# Birmingham Civil Rights National Monument, bicr, National Monument, AL
# Biscayne National Park, bisc, National Park, FL
# Black Canyon Of The Gunnison National Park, blca, National Park, CO
# Blackstone River Valley National Historical Park, blrv, National Historical Park, RI,MA
# Blue Ridge National Heritage Area, blrn, National Heritage Area, NC
# Blue Ridge Parkway, blri, Parkway, NC,VA
# Bluestone National Scenic River, blue, National Scenic River, WV
# Booker T Washington National Monument, bowa, National Monument, VA
# Boston African American National Historic Site, boaf, National Historic Site, MA
# Boston Harbor Islands National Recreation Area, boha, National Recreation Area, MA
# Boston National Historical Park, bost, National Historical Park, MA
# Brices Cross Roads National Battlefield Site, brcr, National Battlefield Site, MS
# Brown v. Board of Education National Historic Site, brvb, National Historic Site, KS
# Bryce Canyon National Park, brca, National Park, UT
# Buck Island Reef National Monument, buis, National Monument, VI
# Buffalo National River, buff, National River, AR
# Cabrillo National Monument, cabr, National Monument, CA
# California National Historic Trail, cali, National Historic Trail, CA,CO,ID,KS,MO,NE,NV,OR,UT,WY
# Camp Nelson National Monument, cane, National Monument, KY
# Canaveral National Seashore, cana, National Seashore, FL
# Cane River Creole National Historical Park, cari, National Historical Park, LA
# Cane River National Heritage Area, crha, National Heritage Area, LA
# Canyon de Chelly National Monument, cach, National Monument, AZ
# Canyonlands National Park, cany, National Park, UT
# Cape Cod National Seashore, caco, National Seashore, MA
# Cape Hatteras National Seashore, caha, National Seashore, NC
# Cape Henry Memorial Part of Colonial National Historical Park, came, Part of Colonial National Historical Park, VA
# Cape Krusenstern National Monument, cakr, National Monument, AK
# Cape Lookout National Seashore, calo, National Seashore, NC
# Capitol Hill Parks, cahi, , DC
# Capitol Reef National Park, care, National Park, UT
# Captain John Smith Chesapeake National Historic Trail, cajo, National Historic Trail, VA,MD,DE,DC,PA,NY
# Capulin Volcano National Monument, cavo, National Monument, NM
# Carl Sandburg Home National Historic Site, carl, National Historic Site, NC
# Carlsbad Caverns National Park, cave, National Park, NM
# Carter G. Woodson Home National Historic Site, cawo, National Historic Site, DC
# Casa Grande Ruins National Monument, cagr, National Monument, AZ
# Castillo de San Marcos National Monument, casa, National Monument, FL
# Castle Clinton National Monument, cacl, National Monument, NY
# Castle Mountains National Monument, camo, National Monument, CA
# Catoctin Mountain Park, cato, Park, MD
# Cedar Breaks National Monument, cebr, National Monument, UT
# Cedar Creek & Belle Grove National Historical Park, cebe, National Historical Park, VA
# César E. Chávez National Monument, cech, National Monument, CA
# Chaco Culture National Historical Park, chcu, National Historical Park, NM
# Chamizal National Memorial, cham, National Memorial, TX
# Champlain Valley National Heritage Partnership, chva, National Heritage Partnership, VT,NY
# Channel Islands National Park, chis, National Park, CA
# Charles Pinckney National Historic Site, chpi, National Historic Site, SC
# Charles Young Buffalo Soldiers National Monument, chyo, National Monument, OH
# Chattahoochee River National Recreation Area, chat, National Recreation Area, GA
# Chesapeake & Ohio Canal National Historical Park, choh, National Historical Park, DC,MD,WV
# Chesapeake Bay, cbpo, , DC,DE,MD,NY,PA,VA,WV
# Chesapeake Bay Gateways and Watertrails Network, cbgn, , DC,MD,NY,PA,VA,WV
# Chickamauga & Chattanooga National Military Park, chch, National Military Park, GA,TN
# Chickasaw National Recreation Area, chic, National Recreation Area, OK
# Chiricahua National Monument, chir, National Monument, AZ
# Christiansted National Historic Site, chri, National Historic Site, VI
# City Of Rocks National Reserve, ciro, National Reserve, ID
# Civil War Defenses of Washington, cwdw, , DC,MD,VA
# Clara Barton National Historic Site, clba, National Historic Site, MD
# Coal National Heritage Area, coal, National Heritage Area, WV
# Colonial National Historical Park, colo, National Historical Park, VA
# Colorado National Monument, colm, National Monument, CO
# Coltsville National Historical Park, colt, National Historical Park, CT
# Congaree National Park, cong, National Park, SC
# Constitution Gardens, coga, , DC
# Coronado National Memorial, coro, National Memorial, AZ
# Cowpens National Battlefield, cowp, National Battlefield, SC
# Crater Lake National Park, crla, National Park, OR
# Craters Of The Moon National Monument & Preserve, crmo, National Monument & Preserve, ID
# Crossroads of the American Revolution National Heritage Area, xrds, National Heritage Area, NJ
# Cumberland Gap National Historical Park, cuga, National Historical Park, KY,TN,VA
# Cumberland Island National Seashore, cuis, National Seashore, GA
# Curecanti National Recreation Area, cure, National Recreation Area, CO
# Cuyahoga Valley National Park, cuva, National Park, OH
# David Berger National Memorial, dabe, National Memorial, OH
# Dayton Aviation Heritage National Historical Park, daav, National Historical Park, OH
# De Soto National Memorial, deso, National Memorial, FL
# Death Valley National Park, deva, National Park, CA,NV
# Delaware & Lehigh National Heritage Corridor, dele, National Heritage Corridor, PA
# Delaware Water Gap National Recreation Area, dewa, National Recreation Area, NJ,PA
# Denali National Park & Preserve, dena, National Park & Preserve, AK
# Devils Postpile National Monument, depo, National Monument, CA
# Devils Tower National Monument, deto, National Monument, WY
# Dinosaur National Monument, dino, National Monument, CO,UT
# Dry Tortugas National Park, drto, National Park, FL
# Ebey's Landing National Historical Reserve, ebla, National Historical Reserve, WA
# Edgar Allan Poe National Historic Site, edal, National Historic Site, PA
# Effigy Mounds National Monument, efmo, National Monument, IA
# Eisenhower National Historic Site, eise, National Historic Site, PA
# El Camino Real de los Tejas National Historic Trail, elte, National Historic Trail, TX,LA
# El Camino Real de Tierra Adentro National Historic Trail, elca, National Historic Trail, NM,TX
# El Malpais National Monument, elma, National Monument, NM
# El Morro National Monument, elmo, National Monument, NM
# Eleanor Roosevelt National Historic Site, elro, National Historic Site, NY
# Ellis Island Part of Statue of Liberty National Monument, elis, Part of Statue of Liberty National Monument, NJ,NY
# Erie Canalway National Heritage Corridor, erie, National Heritage Corridor, NY
# Essex National Heritage Area, esse, National Heritage Area, MA
# Eugene O'Neill National Historic Site, euon, National Historic Site, CA
# Everglades National Park, ever, National Park, FL
# Fallen Timbers Battlefield and Fort Miamis National Historic Site, fati, National Historic Site, OH
# Federal Hall National Memorial, feha, National Memorial, NY
# Fire Island National Seashore, fiis, National Seashore, NY
# First Ladies National Historic Site, fila, National Historic Site, OH
# First State National Historical Park, frst, National Historical Park, DE,PA
# Flight 93 National Memorial, flni, National Memorial, PA
# Florissant Fossil Beds National Monument, flfo, National Monument, CO
# Ford's Theatre, foth, , DC
# Fort Bowie National Historic Site, fobo, National Historic Site, AZ
# Fort Davis National Historic Site, foda, National Historic Site, TX
# Fort Donelson National Battlefield, fodo, National Battlefield, KY,TN
# Fort Dupont Park, fodu, , DC
# Fort Foote Park, fofo, Park, MD
# Fort Frederica National Monument, fofr, National Monument, GA
# Fort Laramie National Historic Site, fola, National Historic Site, WY
# Fort Larned National Historic Site, fols, National Historic Site, KS
# Fort Matanzas National Monument, foma, National Monument, FL
# Fort McHenry National Monument and Historic Shrine, fomc, National Monument and Historic Shrine, MD
# Fort Monroe National Monument, fomr, National Monument, VA
# Fort Necessity National Battlefield, fone, National Battlefield, PA
# Fort Point National Historic Site, fopo, National Historic Site, CA
# Fort Pulaski National Monument, fopu, National Monument, GA
# Fort Raleigh National Historic Site, fora, National Historic Site, NC
# Fort Scott National Historic Site, fosc, National Historic Site, KS
# Fort Smith National Historic Site, fosm, National Historic Site, AR,OK
# Fort Stanwix National Monument, fost, National Monument, NY
# Fort Sumter and Fort Moultrie National Historical Park, fosu, National Historical Park, SC
# Fort Union National Monument, foun, National Monument, NM
# Fort Union Trading Post National Historic Site, fous, National Historic Site, MT,ND
# Fort Vancouver National Historic Site, fova, National Historic Site, OR,WA
# Fort Washington Park, fowa, Park, MD
# Fossil Butte National Monument, fobu, National Monument, WY
# Franklin Delano Roosevelt Memorial, frde, , DC
# Frederick Douglass National Historic Site, frdo, National Historic Site, DC
# Frederick Law Olmsted National Historic Site, frla, National Historic Site, MA
# Fredericksburg & Spotsylvania National Military Park, frsp, National Military Park, VA
# Freedom Riders National Monument, frri, National Monument, AL
# Friendship Hill National Historic Site, frhi, National Historic Site, PA
# Gates Of The Arctic National Park & Preserve, gaar, National Park & Preserve, AK
# Gateway Arch National Park, jeff, National Park, MO
# Gateway National Recreation Area, gate, National Recreation Area, NY,NJ
# Gauley River National Recreation Area, gari, National Recreation Area, WV
# General Grant National Memorial, gegr, National Memorial, NY
# George Rogers Clark National Historical Park, gero, National Historical Park, IN
# George Washington Birthplace National Monument, gewa, National Monument, VA
# George Washington Carver National Monument, gwca, National Monument, MO
# George Washington Memorial Parkway, gwmp, Memorial Parkway, DC,MD,VA
# Gettysburg National Military Park, gett, National Military Park, PA
# Gila Cliff Dwellings National Monument, gicl, National Monument, NM
# Glacier Bay National Park & Preserve, glba, National Park & Preserve, AK
# Glacier National Park, glac, National Park, MT
# Glen Canyon National Recreation Area, glca, National Recreation Area, AZ,UT
# Glen Echo Park, glec, Park, MD
# Gloria Dei Church National Historic Site, glde, National Historic Site, PA
# Golden Gate National Recreation Area, goga, National Recreation Area, CA
# Golden Spike National Historical Park, gosp, National Historical Park, UT
# Governors Island National Monument, gois, National Monument, NY
# Grand Canyon National Park, grca, National Park, AZ
# Grand Portage National Monument, grpo, National Monument, MN
# Grand Teton National Park, grte, National Park, WY
# Grant-Kohrs Ranch National Historic Site, grko, National Historic Site, MT
# Great Basin National Park, grba, National Park, NV
# Great Egg Harbor River, greg, , NJ
# Great Falls Park, grfa, Park, VA
# Great Sand Dunes National Park & Preserve, grsa, National Park & Preserve, CO
# Great Smoky Mountains National Park, grsm, National Park, NC,TN
# Green Springs, grsp, , VA
# Greenbelt Park, gree, Park, MD
# Guadalupe Mountains National Park, gumo, National Park, TX
# Guilford Courthouse National Military Park, guco, National Military Park, NC
# Gulf Islands National Seashore, guis, National Seashore, FL,MS
# Gullah/Geechee Cultural Heritage Corridor, guge, Cultural Heritage Corridor, FL,GA,NC,SC
# Hagerman Fossil Beds National Monument, hafo, National Monument, ID
# Haleakal&#257; National Park, hale, National Park, HI
# Hamilton Grange National Memorial, hagr, National Memorial, NY
# Hampton National Historic Site, hamp, National Historic Site, MD
# Harmony Hall, haha, , MD
# Harpers Ferry National Historical Park, hafe, National Historical Park, WV,VA,MD
# Harriet Tubman National Historical Park, hart, National Historical Park, NY
# Harriet Tubman Underground Railroad National Historical Park, hatu, National Historical Park, MD
# Harry S Truman National Historic Site, hstr, National Historic Site, MO
# Hawai'i Volcanoes National Park, havo, National Park, HI
# Herbert Hoover National Historic Site, heho, National Historic Site, IA
# Historic Jamestowne Part of Colonial National Historical Park, jame, Part of Colonial National Historical Park, VA
# Hohokam Pima National Monument, pima, National Monument, AZ
# Home Of Franklin D Roosevelt National Historic Site, hofr, National Historic Site, NY
# Homestead National Monument of America, home, National Monument of America, NE
# Honouliuli National Historic Site, hono, National Historic Site, HI
# Hopewell Culture National Historical Park, hocu, National Historical Park, OH
# Hopewell Furnace National Historic Site, hofu, National Historic Site, PA
# Horseshoe Bend National Military Park, hobe, National Military Park, AL
# Hot Springs National Park, hosp, National Park, AR
# Hovenweep National Monument, hove, National Monument, CO,UT
# Hubbell Trading Post National Historic Site, hutr, National Historic Site, AZ
# Hudson River Valley National Heritage Area, hurv, National Heritage Area, NY
# I&#241;upiat Heritage Center, inup, , AK
# Ice Age Floods National Geologic Trail, iafl, National Geologic Trail, WA,OR,ID,MT
# Ice Age National Scenic Trail, iatr, National Scenic Trail, WI
# Independence National Historical Park, inde, National Historical Park, PA
# Indiana Dunes National Park, indu, National Park, IN
# Isle Royale National Park, isro, National Park, MI
# James A Garfield National Historic Site, jaga, National Historic Site, OH
# Jean Lafitte National Historical Park and Preserve, jela, National Historical Park and Preserve, LA
# Jewel Cave National Monument, jeca, National Monument, SD
# Jimmy Carter National Historic Site, jica, National Historic Site, GA
# John Day Fossil Beds National Monument, joda, National Monument, OR
# John Fitzgerald Kennedy National Historic Site, jofi, National Historic Site, MA
# John H. Chafee Blackstone River Valley National Heritage Corridor, blac, National Heritage Corridor, MA,RI
# John Muir National Historic Site, jomu, National Historic Site, CA
# Johnstown Flood National Memorial, jofl, National Memorial, PA
# Joshua Tree National Park, jotr, National Park, CA
# Journey Through Hallowed Ground National Heritage Area, jthg, National Heritage Area, MD,PA,WV,VA
# Juan Bautista de Anza National Historic Trail, juba, National Historic Trail, AZ,CA
# Kalaupapa National Historical Park, kala, National Historical Park, HI
# Kaloko-Honok&#333;hau National Historical Park, kaho, National Historical Park, HI
# Katahdin Woods and Waters National Monument, kaww, National Monument, ME
# Katmai National Park & Preserve, katm, National Park & Preserve, AK
# Kenai Fjords National Park, kefj, National Park, AK
# Kenilworth Park & Aquatic Gardens, keaq, , DC
# Kennesaw Mountain National Battlefield Park, kemo, National Battlefield Park, GA
# Keweenaw National Historical Park, kewe, National Historical Park, MI
# Kings Mountain National Military Park, kimo, National Military Park, SC
# Klondike Gold Rush - Seattle Unit National Historical Park, klse, National Historical Park, WA
# Klondike Gold Rush National Historical Park, klgo, National Historical Park, AK
# Knife River Indian Villages National Historic Site, knri, National Historic Site, ND
# Kobuk Valley National Park, kova, National Park, AK
# Korean War Veterans Memorial, kowa, , DC
# Lake Clark National Park & Preserve, lacl, National Park & Preserve, AK
# Lake Mead National Recreation Area, lake, National Recreation Area, AZ,NV
# Lake Meredith National Recreation Area, lamr, National Recreation Area, TX
# Lake Roosevelt National Recreation Area, laro, National Recreation Area, WA
# Lassen Volcanic National Park, lavo, National Park, CA
# Lava Beds National Monument, labe, National Monument, CA
# LBJ Memorial Grove on the Potomac, lyba, , DC
# Lewis & Clark National Historic Trail, lecl, National Historic Trail, IA,ID,IL,IN,KS,KY,MO,MT,NE,ND,OH,OR,PA,SD,WA,WV
# Lewis and Clark National Historical Park, lewi, National Historical Park, OR,WA
# Lincoln Boyhood National Memorial, libo, National Memorial, IN
# Lincoln Home National Historic Site, liho, National Historic Site, IL
# Lincoln Memorial, linc, , DC
# Little Bighorn Battlefield National Monument, libi, National Monument, MT
# Little River Canyon National Preserve, liri, National Preserve, AL
# Little Rock Central High School National Historic Site, chsc, National Historic Site, AR
# Longfellow House Washington's Headquarters National Historic Site, long, National Historic Site, MA
# Lowell National Historical Park, lowe, National Historical Park, MA
# Lower Delaware National Wild and Scenic River, lode, National Wild and Scenic River, PA,NJ
# Lower East Side Tenement Museum National Historic Site, loea, National Historic Site, NY
# Lyndon B Johnson National Historical Park, lyjo, National Historical Park, TX
# Maggie L Walker National Historic Site, mawa, National Historic Site, VA
# Maine Acadian Culture, maac, , ME
# Mammoth Cave National Park, maca, National Park, KY
# Manassas National Battlefield Park, mana, National Battlefield Park, VA
# Manhattan Project National Historical Park, mapr, National Historical Park, NM,WA,TN
# Manzanar National Historic Site, manz, National Historic Site, CA
# Marsh - Billings - Rockefeller National Historical Park, mabi, National Historical Park, VT
# Martin Luther King, Jr. Memorial, mlkm, , DC
# Martin Luther King, Jr. National Historical Park, malu, National Historical Park, GA
# Martin Van Buren National Historic Site, mava, National Historic Site, NY
# Mary McLeod Bethune Council House National Historic Site, mamc, National Historic Site, DC
# Mesa Verde National Park, meve, National Park, CO
# Minidoka National Historic Site, miin, National Historic Site, ID,WA
# Minute Man National Historical Park, mima, National Historical Park, MA
# Minuteman Missile National Historic Site, mimi, National Historic Site, SD
# Mississippi Delta National Heritage Area, mide, National Heritage Area, MS
# Mississippi Gulf National Heritage Area, migu, National Heritage Area, MS
# Mississippi Hills National Heritage Area, mihi, National Heritage Area, MS
# Mississippi National River and Recreation Area, miss, National River and Recreation Area, MN
# Missouri National Recreational River, mnrr, National Recreational River, SD,NE
# Mojave National Preserve, moja, National Preserve, CA
# Monocacy National Battlefield, mono, National Battlefield, MD
# Montezuma Castle National Monument, moca, National Monument, AZ
# Moores Creek National Battlefield, mocr, National Battlefield, NC
# Mormon Pioneer National Historic Trail, mopi, National Historic Trail, IL,IA,NE,UT,WY
# Morristown National Historical Park, morr, National Historical Park, NJ
# Motor Cities National Heritage Area, auto, National Heritage Area, MI
# Mount Rainier National Park, mora, National Park, WA
# Mount Rushmore National Memorial, moru, National Memorial, SD
# Muir Woods National Monument, muwo, National Monument, CA
# Muscle Shoals National Heritage Area, mush, National Heritage Area, AL
# Natchez National Historical Park, natc, National Historical Park, MS
# Natchez Trace National Scenic Trail, natt, National Scenic Trail, AL,MS,TN
# Natchez Trace Parkway, natr, Parkway, AL,MS,TN
# National Aviation Heritage Area, avia, Heritage Area, OH
# National Capital Parks-East, nace, , DC
# National Mall and Memorial Parks, nama, , DC
# National Park of American Samoa, npsa, , AS
# National Parks of New York Harbor, npnh, , NY
# Natural Bridges National Monument, nabr, National Monument, UT
# Navajo National Monument, nava, National Monument, AZ
# New Bedford Whaling National Historical Park, nebe, National Historical Park, MA
# New England National Scenic Trail, neen, National Scenic Trail, MA,CT
# New Jersey Pinelands National Reserve, pine, National Reserve, NJ
# New Orleans Jazz National Historical Park, jazz, National Historical Park, LA
# New River Gorge National River, neri, National River, WV
# Nez Perce National Historical Park, nepe, National Historical Park, ID,MT,OR,WA
# Niagara Falls National Heritage Area, nifa, National Heritage Area, NY
# Nicodemus National Historic Site, nico, National Historic Site, KS
# Ninety Six National Historic Site, nisi, National Historic Site, SC
# Niobrara National Scenic River, niob, National Scenic River, NE
# Noatak National Preserve, noat, National Preserve, AK
# North Cascades National Park, noca, National Park, WA
# North Country National Scenic Trail, noco, National Scenic Trail, MI,MN,ND,NY,OH,PA,VT,WI
# Obed Wild & Scenic River, obed, Wild & Scenic River, TN
# Ocmulgee Mounds National Historical Park, ocmu, National Historical Park, GA
# Oil Region National Heritage Area, oire, National Heritage Area, PA
# Oklahoma City National Memorial, okci, National Memorial, OK
# Old Spanish National Historic Trail, olsp, National Historic Trail, AZ,CA,CO,NV,NM,UT
# Olympic National Park, olym, National Park, WA
# Oregon Caves National Monument & Preserve, orca, National Monument & Preserve, OR
# Oregon National Historic Trail, oreg, National Historic Trail, ID,KS,MO,NE,OR,WA,WY
# Organ Pipe Cactus National Monument, orpi, National Monument, AZ
# Overmountain Victory National Historic Trail, ovvi, National Historic Trail, NC,SC,TN,VA
# Oxon Cove  Park & Oxon Hill Farm, oxhi, , MD
# Ozark National Scenic Riverways, ozar, National Scenic Riverways, MO
# Padre Island National Seashore, pais, National Seashore, TX
# Palo Alto Battlefield National Historical Park, paal, National Historical Park, TX
# Parashant National Monument, para, National Monument, AZ
# Paterson Great Falls National Historical Park, pagr, National Historical Park, NJ
# Pea Ridge National Military Park, peri, National Military Park, AR
# Pearl Harbor National Memorial, valr, National Memorial, HI
# Pecos National Historical Park, peco, National Historical Park, NM
# Pennsylvania Avenue, paav, , DC
# Perry's Victory & International Peace Memorial, pevi, Memorial, OH
# Petersburg National Battlefield, pete, National Battlefield, VA
# Petrified Forest National Park, pefo, National Park, AZ
# Petroglyph National Monument, petr, National Monument, NM
# Pictured Rocks National Lakeshore, piro, National Lakeshore, MI
# Pinnacles National Park, pinn, National Park, CA
# Pipe Spring National Monument, pisp, National Monument, AZ
# Pipestone National Monument, pipe, National Monument, MN
# Piscataway Park, pisc, Park, MD
# Point Reyes National Seashore, pore, National Seashore, CA
# Pony Express National Historic Trail, poex, National Historic Trail, CA,CO,KS,MO,NE,NV,UT,WY
# Port Chicago Naval Magazine National Memorial, poch, National Memorial, CA
# Potomac Heritage National Scenic Trail, pohe, National Scenic Trail, DC,MD,PA,VA
# Poverty Point National Monument, popo, National Monument, LA
# President William Jefferson Clinton Birthplace Home National Historic Site, wicl, National Historic Site, AR
# President's Park (White House), whho, , DC
# Presidio of San Francisco, prsf, , CA
# Prince William Forest Park, prwi, Park, VA
# Pu`uhonua O H&#333;naunau National Historical Park, puho, National Historical Park, HI
# Pu`ukohol&#257; Heiau National Historic Site, puhe, National Historic Site, HI
# Pullman National Monument, pull, National Monument, IL
# Rainbow Bridge National Monument, rabr, National Monument, UT
# Reconstruction Era National Historical Park, reer, National Historical Park, SC
# Redwood National and State Parks, redw, National and State Parks, CA
# Richmond National Battlefield Park, rich, National Battlefield Park, VA
# Rio Grande Wild & Scenic River, rigr, Wild & Scenic River, TX
# River Raisin National Battlefield Park, rira, National Battlefield Park, MI
# Rivers Of Steel National Heritage Area, rist, National Heritage Area, PA
# Rock Creek Park, rocr, Park, DC
# Rocky Mountain National Park, romo, National Park, CO
# Roger Williams National Memorial, rowi, National Memorial, RI
# Roosevelt Campobello International Park, roca, International Park, ME
# Rosie the Riveter WWII Home Front National Historical Park, rori, National Historical Park, CA
# Russell Cave National Monument, ruca, National Monument, AL
# Sagamore Hill National Historic Site, sahi, National Historic Site, NY
# Saguaro National Park, sagu, National Park, AZ
# Saint Croix Island International Historic Site, sacr, International Historic Site, ME
# Saint Croix National Scenic Riverway, sacn, National Scenic Riverway, WI,MN
# Saint Paul's Church National Historic Site, sapa, National Historic Site, NY
# Saint-Gaudens National Historical Park, saga, National Historical Park, NH
# Salem Maritime National Historic Site, sama, National Historic Site, MA
# Salinas Pueblo Missions National Monument, sapu, National Monument, NM
# Salt River Bay National Historical Park and Ecological Preserve, sari, National Historical Park and Ecological Preserve, VI
# San Antonio Missions National Historical Park, saan, National Historical Park, TX
# San Francisco Maritime National Historical Park, safr, National Historical Park, CA
# San Juan Island National Historical Park, sajh, National Historical Park, WA
# San Juan National Historic Site, saju, National Historic Site, PR
# Sand Creek Massacre National Historic Site, sand, National Historic Site, CO
# Santa Fe National Historic Trail, safe, National Historic Trail, CO,KS,MO,NM,OK
# Santa Monica Mountains National Recreation Area, samo, National Recreation Area, CA
# Saratoga National Historical Park, sara, National Historical Park, NY
# Saugus Iron Works National Historic Site, sair, National Historic Site, MA
# Schuylkill River Valley National Heritage Area, scrv, National Heritage Area, PA
# Scotts Bluff National Monument, scbl, National Monument, NE
# Selma To Montgomery National Historic Trail, semo, National Historic Trail, AL
# Sequoia & Kings Canyon National Parks, seki, National Parks, CA
# Shenandoah National Park, shen, National Park, VA
# Shenandoah Valley Battlefields National Historic District, shvb, National Historic District, VA
# Shiloh National Military Park, shil, National Military Park, TN,MS
# Sitka National Historical Park, sitk, National Historical Park, AK
# Sleeping Bear Dunes National Lakeshore, slbe, National Lakeshore, MI
# South Carolina National Heritage Corridor, soca, National Heritage Corridor, SC
# Springfield Armory National Historic Site, spar, National Historic Site, MA
# Star-Spangled Banner National Historic Trail, stsp, National Historic Trail, MD,VA,DC
# Statue Of Liberty National Monument, stli, National Monument, NY
# Steamtown National Historic Site, stea, National Historic Site, PA
# Stones River National Battlefield, stri, National Battlefield, TN
# Stonewall National Monument, ston, National Monument, NY
# Sunset Crater Volcano National Monument, sucr, National Monument, AZ
# Tallgrass Prairie National Preserve, tapr, National Preserve, KS
# Tennessee Civil War National Heritage Area, tecw, National Heritage Area, TN
# Thaddeus Kosciuszko National Memorial, thko, National Memorial, PA
# The Last Green Valley National Heritage Corridor, qush, National Heritage Corridor, CT,MA
# Theodore Roosevelt Birthplace National Historic Site, thrb, National Historic Site, NY
# Theodore Roosevelt Inaugural National Historic Site, thri, National Historic Site, NY
# Theodore Roosevelt Island, this, , DC
# Theodore Roosevelt National Park, thro, National Park, ND
# Thomas Cole National Historic Site, thco, National Historic Site, NY
# Thomas Edison National Historical Park, edis, National Historical Park, NJ
# Thomas Jefferson Memorial, thje, , DC
# Thomas Stone National Historic Site, thst, National Historic Site, MD
# Timpanogos Cave National Monument, tica, National Monument, UT
# Timucuan Ecological & Historic Preserve, timu, Ecological & Historic Preserve, FL
# Tonto National Monument, tont, National Monument, AZ
# Touro Synagogue National Historic Site, tosy, National Historic Site, RI
# Trail Of Tears National Historic Trail, trte, National Historic Trail, AL,AR,GA,IL,KY,MO,NC,OK,TN
# Tule Lake National Monument, tule, National Monument, CA
# Tule Springs Fossil Beds National Monument, tusk, National Monument, NV
# Tumacácori National Historical Park, tuma, National Historical Park, AZ
# Tupelo National Battlefield, tupe, National Battlefield, MS
# Tuskegee Airmen National Historic Site, tuai, National Historic Site, AL
# Tuskegee Institute National Historic Site, tuin, National Historic Site, AL
# Tuzigoot National Monument, tuzi, National Monument, AZ
# Ulysses S Grant National Historic Site, ulsg, National Historic Site, MO
# Upper Delaware Scenic & Recreational River, upde, Scenic & Recreational River, NY,PA
# Valles Caldera National Preserve, vall, National Preserve, NM
# Valley Forge National Historical Park, vafo, National Historical Park, PA
# Vanderbilt Mansion National Historic Site, vama, National Historic Site, NY
# Vicksburg National Military Park, vick, National Military Park, MS,LA
# Vietnam Veterans Memorial, vive, Memorial, DC
# Virgin Islands Coral Reef National Monument, vicr, National Monument, VI
# Virgin Islands National Park, viis, National Park, VI
# Voyageurs National Park, voya, National Park, MN
# Waco Mammoth National Monument, waco, National Monument, TX
# Walnut Canyon National Monument, waca, National Monument, AZ
# War In The Pacific National Historical Park, wapa, National Historical Park, GU
# Washington Monument, wamo, , DC
# Washington-Rochambeau National Historic Trail, waro, National Historic Trail, MA,RI,CT,NY,NJ,PA,DE,MD,VA,DC
# Washita Battlefield National Historic Site, waba, National Historic Site, OK
# Weir Farm National Historic Site, wefa, National Historic Site, CT
# Wheeling National Heritage Area, whee, National Heritage Area, WV
# Whiskeytown National Recreation Area, whis, National Recreation Area, CA
# White Sands National Monument, whsa, National Monument, NM
# Whitman Mission National Historic Site, whmi, National Historic Site, WA
# William Howard Taft National Historic Site, wiho, National Historic Site, OH
# Wilson's Creek National Battlefield, wicr, National Battlefield, MO
# Wind Cave National Park, wica, National Park, SD
# Wing Luke Museum Affiliated Area, wing, Affiliated Area, WA
# Wolf Trap National Park for the Performing Arts, wotr, , VA
# Women's Rights National Historical Park, wori, National Historical Park, NY
# World War II Memorial, wwii, , DC
# Wrangell - St Elias National Park & Preserve, wrst, National Park & Preserve, AK
# Wright Brothers National Memorial, wrbr, National Memorial, NC
# Wupatki National Monument, wupa, National Monument, AZ
# Yellowstone National Park, yell, National Park, ID,MT,WY
# Yorktown Battlefield Part of Colonial National Historical Park, york, Part of Colonial National Historical Park, VA
# Yosemite National Park, yose, National Park, CA
# Yucca House National Monument, yuho, National Monument, CO
# Yukon - Charley Rivers National Preserve, yuch, National Preserve, AK
# Zion National Park, zion, National Park, UT