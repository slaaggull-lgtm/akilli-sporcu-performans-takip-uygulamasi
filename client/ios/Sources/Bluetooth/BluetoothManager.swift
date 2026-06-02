import Foundation
import CoreBluetooth

/// Bluetooth Low Energy (BLE) baglanti ve veri akis yoneticisi.
///
/// Core Bluetooth cercevesini kullanarak giyilebilir sensorlerle
/// (akilli saatler, fitness takip cihazlari) iletisim kurar.
///
/// Standart GATT (Generic Attribute Profile) servis UUID'leri kullanilir:
///   0x180D → Heart Rate Service
///   0x2A37 → Heart Rate Measurement Characteristic
class BluetoothManager: NSObject, ObservableObject, CBCentralManagerDelegate, CBPeripheralDelegate {

    // MARK: - Yayinlanan Ozellikler (SwiftUI icin)

    @Published var connectionStatus: String = "Baglanti Yok"
    @Published var heartRateBPM: Int = 0
    @Published var isConnected: Bool = false

    // MARK: - Ozel Ozellikler

    private var centralManager: CBCentralManager!
    private var heartRatePeripheral: CBPeripheral?

    // BLE Standart UUID'leri
    private let heartRateServiceUUID = CBUUID(string: "180D")
    private let heartRateMeasurementUUID = CBUUID(string: "2A37")

    override init() {
        super.init()
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }

    // MARK: - Tarama Baslat / Durdur

    func startScanning() {
        guard centralManager.state == .poweredOn else { return }
        connectionStatus = "Cihaz Aranıyor..."
        centralManager.scanForPeripherals(
            withServices: [heartRateServiceUUID],
            options: [CBCentralManagerScanOptionAllowDuplicatesKey: false]
        )
    }

    func stopScanning() {
        centralManager.stopScan()
    }

    func disconnect() {
        if let peripheral = heartRatePeripheral {
            centralManager.cancelPeripheralConnection(peripheral)
        }
    }

    // MARK: - CBCentralManagerDelegate

    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        switch central.state {
        case .poweredOn:
            connectionStatus = "Bluetooth Hazir"
            startScanning()
        case .poweredOff:
            connectionStatus = "Bluetooth Kapali"
            isConnected = false
        case .unauthorized:
            connectionStatus = "Bluetooth izni verilmedi"
        case .unsupported:
            connectionStatus = "Bu cihaz BLE desteklemiyor"
        default:
            connectionStatus = "Bilinmeyen durum"
        }
    }

    func centralManager(
        _ central: CBCentralManager,
        didDiscover peripheral: CBPeripheral,
        advertisementData: [String: Any],
        rssi RSSI: NSNumber
    ) {
        let name = peripheral.name ?? "Bilinmeyen Cihaz"
        connectionStatus = "Cihaz Bulundu: \(name)"

        heartRatePeripheral = peripheral
        heartRatePeripheral?.delegate = self
        centralManager.stopScan()
        centralManager.connect(peripheral, options: nil)
    }

    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        let name = peripheral.name ?? "Cihaz"
        connectionStatus = "Baglı: \(name)"
        isConnected = true
        peripheral.discoverServices([heartRateServiceUUID])
    }

    func centralManager(
        _ central: CBCentralManager,
        didDisconnectPeripheral peripheral: CBPeripheral,
        error: Error?
    ) {
        connectionStatus = "Baglanti Kesildi"
        isConnected = false
        heartRateBPM = 0
    }

    func centralManager(
        _ central: CBCentralManager,
        didFailToConnect peripheral: CBPeripheral,
        error: Error?
    ) {
        connectionStatus = "Baglanti Hatasi"
        isConnected = false
    }

    // MARK: - CBPeripheralDelegate

    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        guard error == nil, let services = peripheral.services else { return }
        for service in services {
            peripheral.discoverCharacteristics([heartRateMeasurementUUID], for: service)
        }
    }

    func peripheral(
        _ peripheral: CBPeripheral,
        didDiscoverCharacteristicsFor service: CBService,
        error: Error?
    ) {
        guard error == nil, let characteristics = service.characteristics else { return }
        for characteristic in characteristics {
            if characteristic.uuid == heartRateMeasurementUUID {
                // Notify: Deger her degistiginde otomatik paket gonder
                peripheral.setNotifyValue(true, for: characteristic)
            }
        }
    }

    func peripheral(
        _ peripheral: CBPeripheral,
        didUpdateValueFor characteristic: CBCharacteristic,
        error: Error?
    ) {
        if let error = error {
            print("BLE veri okuma hatasi: \(error.localizedDescription)")
            return
        }

        if characteristic.uuid == heartRateMeasurementUUID,
           let data = characteristic.value {
            let bpm = decodeHeartRate(from: data)
            DispatchQueue.main.async {
                self.heartRateBPM = bpm
            }
        }
    }

    // MARK: - Yardimci Fonksiyonlar

    /// Standart BLE Heart Rate Measurement formatini cozumler.
    /// Birinci byte flag byte'idir; ikinci byte BPM degerini icerir (8-bit format).
    private func decodeHeartRate(from data: Data) -> Int {
        let bytes = [UInt8](data)
        guard bytes.count >= 2 else { return 0 }

        // Flag byte'in 0. biti: 0 = 8-bit HR, 1 = 16-bit HR
        let is16Bit = (bytes[0] & 0x01) == 1
        if is16Bit && bytes.count >= 3 {
            return Int(bytes[1]) + (Int(bytes[2]) << 8)
        } else {
            return Int(bytes[1])
        }
    }
}
