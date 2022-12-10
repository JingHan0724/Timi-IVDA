import * as echarts from 'echarts';
import usaJson from '../assets/USA.json'
export function myEcharts(dom,data, sharch) {

    // let ROOT_PATH = 'https://echarts.apache.org/examples';

    var chartDom = document.getElementById(dom);

    
    var myChart = echarts.init(chartDom);

    //myChart.resize()
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
                    '#FBEEE6',
                    '#F6DDCC',
                    '#EDBB99',
                    '#F0B27A',
                    '#DC7633',
                    '#D35400',
                    '#fee090',
                    '#BA4A00',
                    '#A04000',
                    '#873600',
                    '#6E2C00'
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

    

