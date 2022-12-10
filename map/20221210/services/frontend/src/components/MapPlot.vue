<template>
  <div id="MapPlot" style="height: inherit" >
    <div class="item">
      <div id="char" style="width: auto;height:650px;"></div>
      <!--      <div id="line"></div>-->
      <div class="search">
        <el-select @change="changeFun" v-model="sharch" placeholder="Please select:">
          <el-option
              v-for="item in headList"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </div>
    </div>
  </div>
</template>

<script>
import {myEcharts} from '../util/util'
import axios from 'axios'
export default {
  name: 'MapPlot',
  components: {
},
  data() {
    return {
      address:[
        { label: 'Alabama', value: 'AL'},
        { label: 'Alaska', value: 'AK'},
        { label: 'Arizona', value: 'AZ'},
        { label: 'Arkansas', value: 'AR'},
        { label: 'California', value: 'CA'},
        { label: 'Colorado', value: 'CO'},
        { label: 'Connecticut', value: 'CT'},
        { label: 'Delaware', value: 'DE'},
        { label: 'District of Columbia', value: '	DC'},
        { label: 'Florida', value: 'FL'},
        { label: 'Georgia', value: 'GA'},
        { label: 'Hawaii', value: 'HI'},
        { label: 'Idaho', value: 'ID'},
        { label: 'Illinois', value: 'IL'},

        { label: 'Indiana', value: 'IN'},
        { label: 'Iowa', value: 'IA'},
        { label: 'Kansas', value: 'KS'},
        { label: 'Kentucky', value: 'KY'},
        { label: 'Louisiana', value: 'LA'},
        { label: 'Maine', value: 'ME'},

        // { label: 'Maine', value: 'ME'},
        { label: 'Maryland', value: 'MD'},
        { label: 'Massachusetts', value: 'MA'},
        { label: 'Michigan', value: 'MI'},
        { label: 'Minnesota', value: 'MN'},
        { label: 'Mississippi', value: 'MS'},
        { label: 'Missouri', value: 'MO'},
        { label: 'Montana', value: 'MT'},
        { label: 'Nebraska', value: 'NE'},
        { label: 'Nevada', value: 'NV'},

        { label: 'New Hampshire', value: 'NH'},
        { label: 'New Jersey', value: 'NJ'},
        { label: 'New Mexico', value: 'NM'},
        { label: 'New York', value: 'NY'},
        { label: 'North Carolina', value: 'NC'},
        { label: 'North Dakota', value: 'ND'},
        { label: 'Ohio', value: 'OH'},
        { label: 'Oklahoma', value: 'OK'},
        { label: 'Oregon', value: 'OR'},
        { label: 'Pennsylvania', value: 'PA'},
        { label: 'Puerto Rico', value: 'PR'},

        { label: 'Rhode Island', value: 'RI'},
        { label: 'South Carolina', value: 'SC'},
        { label: 'South Dakota', value: 'SD'},
        { label: 'Tennessee', value: 'TN'},
        { label: 'Texas', value: 'TX'},
        { label: 'Utah', value: 'UT'},
        { label: 'Vermont', value: 'VT'},
        { label: 'Virginia', value: 'VA'},
        { label: 'Washington', value: 'WA'},
        { label: 'West Virginia', value: 'WV'},
        { label: 'Wisconsin', value: 'WI'},
        { label: 'Wyoming', value: 'WY'},


      ],
      list: [],
      headList: [],
      sharch: ''
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    getData() {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:5000',
        data: {
          sharch: this.sharch
        }
      }).then(res => {
        this.list = []
        res.data.forEach(el => {
          this.address.forEach(els => {
            if(els.value === el.address) {
              this.list.push({
                name: els.label,
                value: el.key.toFixed(2)
              })
            }
          })
        })
        myEcharts('char',this.list, this.sharch)
        // console.log(this.list)
      })
    },

    changeFun() {
      this.getData()
    },
    getList() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:5000/list',
      }).then(res => {
        // let l = 5
        res.data.shift()
        this.headList = []
        res.data.forEach((el,index) => {
          let obj = {
            label: el,
            value: el
          }
          this.headList.push(obj)
          if(index === 0) {
            this.sharch = el
          }

        })

        this.getData()
      })
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  justify-content: center;

}

.item {
  width: 800px;
  position: relative;
}

#char {
  width: 100%;
  height: 600px;
}

.search {
  position: absolute;
  top: 0;
}
</style>