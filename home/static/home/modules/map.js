import {
    updateSelectedStore,
} from './stores.js';

mapboxgl.accessToken = 'pk.eyJ1Ijoia2F5Y2VlMzI4IiwiYSI6ImNsempvNXppbjB0dHEyanNpczEwYjNhMWQifQ.6CkB76_2aMw5z4Woj8jt6g';

/**
 * @typedef {import('./api').Store} Store
 */

/**
 * Stores GeoJSON Feature object
 * @typedef {Object} StoreFeatureObject
 * @property {'Feature'} type
 * @property {{type: 'Point', coordinates: [number, number] }} geometry
 * @property {Store} properties
 */

/**
 * Stores GeoJSON FeatureCollection
 * @typedef {Object} StoresGeoJSON
 * @property {'FeatureCollection'} type
 * @property {StoreFeatureObject[]} features
 */

/**
 * Create a new mapbox map instance
 * @return {Object} Map
 */
export function addMap() {
    const map = new mapboxgl.Map({  
        container: 'map',  
        style: 'mapbox://styles/mapbox/light-v10',  
        center: [77.645296, 12.978624],  
        zoom: 2  
    });
    
    map.addControl(new mapboxgl.NavigationControl());  
    
    return map;
}

/**
 * Add a geoCoder control to a mapbox map
 * @param {Object} map
 * @param {function} geocoderCallback - The callback that handles the response.
 */
export function addGeocoder(map, geocoderCallback) {
    const geocoder = new MapboxGeocoder({ accessToken: mapboxgl.accessToken, mapboxgl: mapboxgl });map.addControl(geocoder);geocoder.on("result", (data) => {  
        geocoderCallback(data);  
    });
}

/**
 * Converts array of stores to GeoJSON format
 * @param {Store[]} stores
 * @return {StoresGeoJSON} Stores in GeoJSON
 */
export function convertToGeoJson(stores) {
    return {}
}

/**
 * Display stores on map
 * @param {Object} map
 * @param {StoresGeoJSON} storesGeoJson
 */
export function plotStoresOnMap(map, storesGeoJson) {
    
}

/**
 * Zoom in-to a specific point on a map
 * @param {Object} map
 * @param {StoreFeatureObject} point
 */
export function flyToStore(map, point) {

}

/**
 * Display store info on the map using a popup
 * @param {Object} map
 * @param {StoreFeatureObject} point
 */
export function displayStoreDetails(map, point) {
    
}
