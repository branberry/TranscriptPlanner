<template>
  <div class="sidebar"
       :data="backgroundColor">
    <!--
            Tip 1: you can change the color of the sidebar's background using: data-background-color="white | black | darkblue"
            Tip 2: you can change the color of the active button using the data-active-color="primary | info | success | warning | danger"
        -->
    <!-- -->
    <div class="sidebar-wrapper" id="style-3">
      <div class="logo">
        <a href="http://augsburg.edu" class="simple-text logo-mini">
          <div class="logo-img"
               :class="{'logo-img-rtl': $rtl.isRTL}">
            <img
              src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAAA8AAD/4QMxaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzEzOCA3OS4xNTk4MjQsIDIwMTYvMDkvMTQtMDE6MDk6MDEgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE3IChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkEwMjI2ODAxM0E5NDExRTc4OUQ0QUE5RTI3NEQ2Rjk5IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkEwMjI2ODAyM0E5NDExRTc4OUQ0QUE5RTI3NEQ2Rjk5Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6QTAyMjY3RkYzQTk0MTFFNzg5RDRBQTlFMjc0RDZGOTkiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QTAyMjY4MDAzQTk0MTFFNzg5RDRBQTlFMjc0RDZGOTkiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7/7gAOQWRvYmUAZMAAAAAB/9sAhAAGBAQEBQQGBQUGCQYF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"
              alt="">
          </div>
        </a>
        <a href="http://augsburg.edu" class="simple-text logo-normal">
          {{title}}
        </a>
      </div>
      <slot>

      </slot>
      <ul class="nav">
        <!--By default vue-router adds an active class to each route link. This way the links are colored when clicked-->
        <slot name="links">
          <sidebar-link v-for="(link,index) in sidebarLinks"
                        :key="index"
                        :to="link.path"
                        :name="link.name"
                        :icon="link.icon">
          </sidebar-link>
        </slot>
      </ul>
    </div>
  </div>
</template>
<script>
  import SidebarLink from "./SidebarLink";

  export default {
    props: {
      title: {
        type: String,
        default: "Augsburg"
      },
      backgroundColor: {
        type: String,
        default: "vue"
      },
      activeColor: {
        type: String,
        default: "success",
        validator: value => {
          let acceptedValues = [
            "primary",
            "info",
            "success",
            "warning",
            "danger"
          ];
          return acceptedValues.indexOf(value) !== -1;
        }
      },
      sidebarLinks: {
        type: Array,
        default: () => []
      },
      autoClose: {
        type: Boolean,
        default: true
      }
    },
    provide() {
      return {
        autoClose: this.autoClose,
        addLink: this.addLink,
        removeLink: this.removeLink
      };
    },
    components: {
      SidebarLink
    },
    computed: {
      /**
       * Styles to animate the arrow near the current active sidebar link
       * @returns {{transform: string}}
       */
      arrowMovePx() {
        return this.linkHeight * this.activeLinkIndex;
      },
      shortTitle() {
        return this.title.split(' ')
          .map(word => word.charAt(0))
          .join('').toUpperCase();
      }
    },
    data() {
      return {
        linkHeight: 65,
        activeLinkIndex: 0,
        windowWidth: 0,
        isWindows: false,
        hasAutoHeight: false,
        links: []
      };
    },
    methods: {
      findActiveLink() {
        this.links.forEach((link, index) => {
          if (link.isActive()) {
            this.activeLinkIndex = index;
          }
        });
      },
      addLink(link) {
        const index = this.$slots.links.indexOf(link.$vnode);
        this.links.splice(index, 0, link);
      },
      removeLink(link) {
        const index = this.links.indexOf(link);
        if (index > -1) {
          this.links.splice(index, 1);
        }
      }
    },
    mounted() {
      this.$watch("$route", this.findActiveLink, {
        immediate: true
      });
    }
  };
</script>
