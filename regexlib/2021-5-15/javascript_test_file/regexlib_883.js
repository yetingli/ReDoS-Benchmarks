/* 883
 * (?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"public: void __thiscall ::::("+"!"*16+"! _1_NQ"
 */
var REGEX = /(?<expo>public\:|protected\:|private\:) (?<ret>(const )*(void|int|unsigned int|long|unsigned long|float|double|(class .*)|(enum .*))) (?<decl>__thiscall|__cdecl|__stdcall|__fastcall|__clrcall) (?<ns>.*)\:\:(?<class>(.*)((<.*>)*))\:\:(?<method>(.*)((<.*>)*))\((?<params>((.*(<.*>)?)(,)?)*)\)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'public: void __thiscall ::::(' + '!'.repeat(i*1) + '! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}