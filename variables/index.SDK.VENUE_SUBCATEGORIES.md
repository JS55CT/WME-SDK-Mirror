---
title: SDK.VENUE_SUBCATEGORIES variable
source: variables/index.SDK.VENUE_SUBCATEGORIES.html
created: 2026-03-11
tool: extract-to-md.py
notes: Extracted from Waze SDK HTML docs. Cleaned for LLM context.
---

# Variable VENUE_SUBCATEGORIESConst

```typescript
VENUE_SUBCATEGORIES: {
  Â Â Â Â CAR_SERVICES: (
  Â Â Â Â Â Â Â Â | "CAR_WASH"
  Â Â Â Â Â Â Â Â | "CHARGING_STATION"
  Â Â Â Â Â Â Â Â | "GARAGE_AUTOMOTIVE_SHOP"
  Â Â Â Â Â Â Â Â | "GAS_STATION"
  Â Â Â Â ) [] ;
  Â Â Â Â CRISIS_LOCATIONS: ( "DONATION_CENTERS" | "SHELTER_LOCATIONS" ) [] ;
  Â Â Â Â CULTURE_AND_ENTERTAINEMENT: readonly [
  Â Â Â Â Â Â Â Â "ART_GALLERY" ,
  Â Â Â Â Â Â Â Â "CASINO" ,
  Â Â Â Â Â Â Â Â "CLUB" ,
  Â Â Â Â Â Â Â Â "TOURIST_ATTRACTION_HISTORIC_SITE" ,
  Â Â Â Â Â Â Â Â "MOVIE_THEATER" ,
  Â Â Â Â Â Â Â Â "MUSEUM" ,
  Â Â Â Â Â Â Â Â "MUSIC_VENUE" ,
  Â Â Â Â Â Â Â Â "PERFORMING_ARTS_VENUE" ,
  Â Â Â Â Â Â Â Â "GAME_CLUB" ,
  Â Â Â Â Â Â Â Â "STADIUM_ARENA" ,
  Â Â Â Â Â Â Â Â "THEME_PARK" ,
  Â Â Â Â Â Â Â Â "ZOO_AQUARIUM" ,
  Â Â Â Â Â Â Â Â "RACING_TRACK" ,
  Â Â Â Â Â Â Â Â "THEATER" ,
  Â Â Â Â ] ;
  Â Â Â Â FOOD_AND_DRINK: readonly [
  Â Â Â Â Â Â Â Â "RESTAURANT" ,
  Â Â Â Â Â Â Â Â "BAKERY" ,
  Â Â Â Â Â Â Â Â "DESSERT" ,
  Â Â Â Â Â Â Â Â "CAFE" ,
  Â Â Â Â Â Â Â Â "FAST_FOOD" ,
  Â Â Â Â Â Â Â Â "FOOD_COURT" ,
  Â Â Â Â Â Â Â Â "BAR" ,
  Â Â Â Â Â Â Â Â "ICE_CREAM" ,
  Â Â Â Â ] ;
  Â Â Â Â LODGING: readonly [
  Â Â Â Â Â Â Â Â "HOTEL" ,
  Â Â Â Â Â Â Â Â "HOSTEL" ,
  Â Â Â Â Â Â Â Â "CAMPING_TRAILER_PARK" ,
  Â Â Â Â Â Â Â Â "COTTAGE_CABIN" ,
  Â Â Â Â Â Â Â Â "BED_AND_BREAKFAST" ,
  Â Â Â Â ] ;
  Â Â Â Â NATURAL_FEATURES: readonly [
  Â Â Â Â Â Â Â Â "ISLAND" ,
  Â Â Â Â Â Â Â Â "SEA_LAKE_POOL" ,
  Â Â Â Â Â Â Â Â "RIVER_STREAM" ,
  Â Â Â Â Â Â Â Â "FOREST_GROVE" ,
  Â Â Â Â Â Â Â Â "FARM" ,
  Â Â Â Â Â Â Â Â "CANAL" ,
  Â Â Â Â Â Â Â Â "SWAMP_MARSH" ,
  Â Â Â Â Â Â Â Â "DAM" ,
  Â Â Â Â ] ;
  Â Â Â Â OTHER: readonly [ "CONSTRUCTION_SITE" ] ;
  Â Â Â Â OUTDOORS: readonly [
  Â Â Â Â Â Â Â Â "PARK" ,
  Â Â Â Â Â Â Â Â "PLAYGROUND" ,
  Â Â Â Â Â Â Â Â "BEACH" ,
  Â Â Â Â Â Â Â Â "SPORTS_COURT" ,
  Â Â Â Â Â Â Â Â "GOLF_COURSE" ,
  Â Â Â Â Â Â Â Â "PLAZA" ,
  Â Â Â Â Â Â Â Â "PROMENADE" ,
  Â Â Â Â Â Â Â Â "POOL" ,
  Â Â Â Â Â Â Â Â "SCENIC_LOOKOUT_VIEWPOINT" ,
  Â Â Â Â Â Â Â Â "SKI_AREA" ,
  Â Â Â Â ] ;
  Â Â Â Â PARKING_LOT: never [] ;
  Â Â Â Â PROFESSIONAL_AND_PUBLIC: readonly [
  Â Â Â Â Â Â Â Â "COLLEGE_UNIVERSITY" ,
  Â Â Â Â Â Â Â Â "SCHOOL" ,
  Â Â Â Â Â Â Â Â "CONVENTIONS_EVENT_CENTER" ,
  Â Â Â Â Â Â Â Â "GOVERNMENT" ,
  Â Â Â Â Â Â Â Â "LIBRARY" ,
  Â Â Â Â Â Â Â Â "CITY_HALL" ,
  Â Â Â Â Â Â Â Â "ORGANIZATION_OR_ASSOCIATION" ,
  Â Â Â Â Â Â Â Â "PRISON_CORRECTIONAL_FACILITY" ,
  Â Â Â Â Â Â Â Â "COURTHOUSE" ,
  Â Â Â Â Â Â Â Â "CEMETERY" ,
  Â Â Â Â Â Â Â Â "FIRE_DEPARTMENT" ,
  Â Â Â Â Â Â Â Â "POLICE_STATION" ,
  Â Â Â Â Â Â Â Â "MILITARY" ,
  Â Â Â Â Â Â Â Â "HOSPITAL_URGENT_CARE" ,
  Â Â Â Â Â Â Â Â "DOCTOR_CLINIC" ,
  Â Â Â Â Â Â Â Â "OFFICES" ,
  Â Â Â Â Â Â Â Â "POST_OFFICE" ,
  Â Â Â Â Â Â Â Â "RELIGIOUS_CENTER" ,
  Â Â Â Â Â Â Â Â "KINDERGARDEN" ,
  Â Â Â Â Â Â Â Â "FACTORY_INDUSTRIAL" ,
  Â Â Â Â Â Â Â Â "EMBASSY_CONSULATE" ,
  Â Â Â Â Â Â Â Â "INFORMATION_POINT" ,
  Â Â Â Â Â Â Â Â "EMERGENCY_SHELTER" ,
  Â Â Â Â Â Â Â Â "TRASH_AND_RECYCLING_FACILITIES" ,
  Â Â Â Â ] ;
  Â Â Â Â SHOPPING_AND_SERVICES: readonly [
  Â Â Â Â Â Â Â Â "ARTS_AND_CRAFTS" ,
  Â Â Â Â Â Â Â Â "BANK_FINANCIAL" ,
  Â Â Â Â Â Â Â Â "SPORTING_GOODS" ,
  Â Â Â Â Â Â Â Â "BOOKSTORE" ,
  Â Â Â Â Â Â Â Â "PHOTOGRAPHY" ,
  Â Â Â Â Â Â Â Â "CAR_DEALERSHIP" ,
  Â Â Â Â Â Â Â Â "FASHION_AND_CLOTHING" ,
  Â Â Â Â Â Â Â Â "CONVENIENCE_STORE" ,
  Â Â Â Â Â Â Â Â "PERSONAL_CARE" ,
  Â Â Â Â Â Â Â Â "DEPARTMENT_STORE" ,
  Â Â Â Â Â Â Â Â "PHARMACY" ,
  Â Â Â Â Â Â Â Â "ELECTRONICS" ,
  Â Â Â Â Â Â Â Â "FLOWERS" ,
  Â Â Â Â Â Â Â Â "FURNITURE_HOME_STORE" ,
  Â Â Â Â Â Â Â Â "GIFTS" ,
  Â Â Â Â Â Â Â Â "GYM_FITNESS" ,
  Â Â Â Â Â Â Â Â "SWIMMING_POOL" ,
  Â Â Â Â Â Â Â Â "HARDWARE_STORE" ,
  Â Â Â Â Â Â Â Â "MARKET" ,
  Â Â Â Â Â Â Â Â "SUPERMARKET_GROCERY" ,
  Â Â Â Â Â Â Â Â "JEWELRY" ,
  Â Â Â Â Â Â Â Â "LAUNDRY_DRY_CLEAN" ,
  Â Â Â Â Â Â Â Â "SHOPPING_CENTER" ,
  Â Â Â Â Â Â Â Â "MUSIC_STORE" ,
  Â Â Â Â Â Â Â Â "PET_STORE_VETERINARIAN_SERVICES" ,
  Â Â Â Â Â Â Â Â "TOY_STORE" ,
  Â Â Â Â Â Â Â Â "TRAVEL_AGENCY" ,
  Â Â Â Â Â Â Â Â "ATM" ,
  Â Â Â Â Â Â Â Â "CURRENCY_EXCHANGE" ,
  Â Â Â Â Â Â Â Â "CAR_RENTAL" ,
  Â Â Â Â Â Â Â Â "TELECOM" ,
  Â Â Â Â ] ;
  Â Â Â Â TRANSPORTATION: readonly [
  Â Â Â Â Â Â Â Â "AIRPORT" ,
  Â Â Â Â Â Â Â Â "BUS_STATION" ,
  Â Â Â Â Â Â Â Â "FERRY_PIER" ,
  Â Â Â Â Â Â Â Â "SEAPORT_MARINA_HARBOR" ,
  Â Â Â Â Â Â Â Â "SUBWAY_STATION" ,
  Â Â Â Â Â Â Â Â "TRAIN_STATION" ,
  Â Â Â Â Â Â Â Â "BRIDGE" ,
  Â Â Â Â Â Â Â Â "TUNNEL" ,
  Â Â Â Â Â Â Â Â "TAXI_STATION" ,
  Â Â Â Â Â Â Â Â "JUNCTION_INTERCHANGE" ,
  Â Â Â Â Â Â Â Â "REST_AREAS" ,
  Â Â Â Â Â Â Â Â "CARPOOL_SPOT" ,
  Â Â Â Â ] ;
} = ...
```
#### Members
| Name | Type/Value | Tags |
|------|------------|------|
| CAR_SERVICES | "CAR_WASH" |  |
| CRISIS_LOCATIONS | "DONATION_CENTERS" |  |
| CULTURE_AND_ENTERTAINEMENT | "ART_GALLERY" |  |
| FOOD_AND_DRINK | "RESTAURANT" |  |
| LODGING | "HOTEL" |  |
| NATURAL_FEATURES | "ISLAND" |  |
| OTHER | "CONSTRUCTION_SITE" |  |
| OUTDOORS | "PARK" |  |
| PARKING_LOT | never |  |
| PROFESSIONAL_AND_PUBLIC | "COLLEGE_UNIVERSITY" |  |
| SHOPPING_AND_SERVICES | "ARTS_AND_CRAFTS" |  |
| TRANSPORTATION | "AIRPORT" |  |
