import * as echarts from 'echarts';
import usaJson from '../assets/USA.json'
export function myEcharts(dom,data, sharch) {

    // let ROOT_PATH = 'https://echarts.apache.org/examples';

    var chartDom = document.getElementById(dom);

    
    var myChart = echarts.init(chartDom);

    myChart.resize()
    let option;

    echarts.registerMap('USA', usaJson, {
        Alaska: {
          left: -131,
          top: 25,
          width: 15
        },
        Hawaii: {
          left: -110,
          top: 28,
          width: 5
        },
        'Puerto Rico': {
          left: -76,
          top: 26,
          width: 2
        }
    });

    option = {
        title: {
            text: 'Health Condition by State',
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2
        },
        visualMap: {
            left: 'right',
            min: 10,
            max: 30,
            inRange: {
                color: [
                '#313695',
                '#4575b4',
                '#74add1',
                '#abd9e9',
                '#e0f3f8',
                '#ffffbf',
                '#fee090',
                '#fdae61',
                '#f46d43',
                '#d73027',
                '#a50026'
                ]
            },
            text: ['High', 'Low'],
            calculable: true
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: { readOnly: false },
                restore: {},
                saveAsImage: {}
            }
        },
        series: [
            {
                name: sharch,
                type: 'map',
                roam: true,
                map: 'USA',
                emphasis: {
                    label: {
                        show: true
                    }
                },
                data: data
            }
        ]
    };
    myChart.setOption(option);
    option && myChart.setOption(option);


    window.onresize = function(){
        myChart.resize();
     
    }
}

    

