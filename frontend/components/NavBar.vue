<template>
         <v-navigation-drawer
      v-model="drawer"
      app
    >
         <v-navigation-drawer permanent>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Application
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item

          <v-list-item-icon>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <!-- <v-list-item-title>{{ item.title }}</v-list-item-title> -->
        <v-list-item-title>
          <NuxtLink :to="{ name: 'sobre' }">Sobre</NuxtLink></v-list-item-title>
            
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard' },
          { title: 'Photos', icon: 'mdi-image' },
          { title: 'About', icon: 'mdi-help-box' },
        ],
      right: null,
      miniVariant: false,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>