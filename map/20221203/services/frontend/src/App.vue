<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h2>CDC 500 Cities</h2>
    </v-app-bar>
    <v-main>
      <MapPlot/>
    </v-main>
  </v-app>
</template>

<script>
import MapPlot from './components/MapPlot';

export default {
  name: 'App',
  components: {
    MapPlot,
  },
  data: () => ({
    //
  }),
};
</script>
<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}

html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}
</style>

