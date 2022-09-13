Os dejo el contenido del external adapter para Zigbee2MQTT
Aquí toda la info sobre como incluirlo: https://www.zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html


```
const fz = require('zigbee-herdsman-converters/converters/fromZigbee');
const tz = require('zigbee-herdsman-converters/converters/toZigbee');
const exposes = require('zigbee-herdsman-converters/lib/exposes');
const reporting = require('zigbee-herdsman-converters/lib/reporting');
const extend = require('zigbee-herdsman-converters/lib/extend');
const e = exposes.presets;
const ea = exposes.access;


const fzLocal = {
    aqara_trv: {
        cluster: 'aqaraOpple',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const result = {};
            Object.entries(msg.data).forEach(([key, value]) => {
                switch (parseInt(key)) {
                case 0x0271:
                    result['state'] = {1: 'ON', 0: 'OFF'}[value];
                    break;
                case 0x0272:
                    result['preset'] = {2: 'away', 1: 'auto', 0: 'manual'}[value];
                    break;
                case 0x0273:
                    result['window_detection'] = {1: 'ON', 0: 'OFF'}[value];
                    break;
                case 0x0274:
                    result['valve_detection'] = {1: 'ON', 0: 'OFF'}[value];
                    break;
                case 0x0277:
                    result['child_lock'] = {1: 'LOCK', 0: 'UNLOCK'}[value];
                    break;
                case 0x0279:
                    result['away_preset_temperature'] = (value / 100).toFixed(1);
                    break;
                case 0x027b:
                    result['calibration'] = {1: true, 0: false}[value];
                    break;
                case 0x027e:
                    result['sensor'] = {1: 'external', 0: 'internal'}[value];
                    break;
                case 0x00ff: // 4e:27:49:bb:24:b6:30:dd:74:de:53:76:89:44:c4:81
                case 0x00f7: // 03:28:1f:05:21:01:00:0a:21:00:00:0d:23:19:08:00:00:11:23...
                case 0x0275: // 0x00000001
                case 0x0276: // 04:3e:01:e0:00:00:09:60:04:38:00:00:06:a4:05:64:00:00:08:98:81:e0:00:00:08:98
                case 0x027a: // 0x00
                case 0x027c: // 0x00
                case 0x027d: // 0x00
                case 0x0280: // 0x00/0x01
                case 0x040a: // 0x64
                    meta.logger.debug(`zigbee-herdsman-converters:aqara_trv: Unhandled key ${key} = ${value}`);
                    break;
                default:
                    meta.logger.warn(`zigbee-herdsman-converters:aqara_trv: Unknown key ${key} = ${value}`);
                }
            });
            return result;
        },
    },
};


const tzLocal = {
    aqara_trv: {
        key: ['state', 'preset', 'window_detection', 'valve_detection', 'child_lock', 'away_preset_temperature'],
        convertSet: async (entity, key, value, meta) => {
            switch (key) {
            case 'state':
                await entity.write('aqaraOpple', {0x0271: {value: {'OFF': 0, 'ON': 1}[value], type: 0x20}},
                    {manufacturerCode: 0x115f});
                break;
            case 'preset':
                await entity.write('aqaraOpple', {0x0272: {value: {'manual': 0, 'auto': 1, 'away': 2}[value], type: 0x20}},
                    {manufacturerCode: 0x115f});
                break;
            case 'window_detection':
                await entity.write('aqaraOpple', {0x0273: {value: {'OFF': 0, 'ON': 1}[value], type: 0x20}},
                    {manufacturerCode: 0x115f});
                break;
            case 'valve_detection':
                await entity.write('aqaraOpple', {0x0274: {value: {'OFF': 0, 'ON': 1}[value], type: 0x20}},
                    {manufacturerCode: 0x115f});
                break;
            case 'child_lock':
                await entity.write('aqaraOpple', {0x0277: {value: {'UNLOCK': 0, 'LOCK': 1}[value], type: 0x20}},
                    {manufacturerCode: 0x115f});
                break;
            case 'away_preset_temperature':
                await entity.write('aqaraOpple', {0x0279: {value: Math.round(value * 100), type: 0x23}}, {manufacturerCode: 0x115f});
                break;
            default: // Unknown key
                meta.logger.warn(`zigbee-herdsman-converters:aqara_trv: Unhandled key ${key}`);
            }
        },
    },
};


const definition = {
    zigbeeModel: ['lumi.airrtc.agl001'],
        model: 'SRTS-A01',
        vendor: 'Xiaomi',
        description: 'Aqara Smart Radiator Thermostat E1',
        fromZigbee: [fzLocal.aqara_trv, fz.thermostat],
        toZigbee: [tzLocal.aqara_trv, tz.thermostat_occupied_heating_setpoint],
        exposes: [e.switch().setAccess('state', ea.STATE_SET),
            exposes.climate().withSetpoint('occupied_heating_setpoint', 5, 30, 0.5)
                .withLocalTemperature(ea.STATE).withPreset(['manual', 'away', 'auto'], ea.STATE_SET),
            e.child_lock(), e.window_detection(), e.valve_detection(),
            e.away_preset_temperature(),
        ],
};

module.exports = definition;

```
