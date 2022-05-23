<template>
  <v-app dark>

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
      <v-list-item >
          <v-list-item-icon>
            <v-icon>mdi-image</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>
               <NuxtLink :to="{ name: 'sobre' }">Sobre</NuxtLink></v-list-item-title> 
            </v-list-item-title>

        <!-- <v-list-item-title> -->
          <!-- <NuxtLink :to="{ name: 'sobre' }">Sobre</NuxtLink></v-list-item-title> -->
            
          </v-list-item-content>

      </v-list-item>

<!-- 
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          
        >
          
        <nuxt-link :to="item.route"></nuxt-link>

          <v-list-item-icon>
            <v-icon>mdi-image</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}
            </v-list-item-title>
        <v-list-item-title> 
         
            
          </v-list-item-content>
        </v-list-item> -->
      </v-list>
    </v-navigation-drawer>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Detector de Fake News</v-toolbar-title>
    </v-app-bar>
      
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
   
    <v-footer
      :absolute="!fixed"
      app
    >
      <span style="text-align: center !important;">Fabricio L. Covalesci &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>


<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', route: "home" },
          { title: 'Sobre', icon: 'mdi-image', route: "sobre" },
          { title: 'About', icon: 'mdi-help-box', route: "about" },
        ],
      right: null,
      miniVariant: false,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>
