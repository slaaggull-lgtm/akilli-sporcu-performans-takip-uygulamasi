import Foundation
import os.signpost

/// CPU ve bellek kullanimini olcen performans izleme sinifi.
/// Singleton desen — uygulamada tek ornek kullanilir.
class PerformanceMonitor {

    static let shared = PerformanceMonitor()

    private let log = OSLog(subsystem: "com.akillitakip.app", category: "Performance")

    // Olculen sure degerleri — label'a gore gruplu
    private var metrics: [String: [Double]] = [:]

    // Thread-safe erisim icin concurrent kuyruk
    private let queue = DispatchQueue(label: "performance.monitor", attributes: .concurrent)

    private init() {}

    // MARK: - CPU Kullanimi

    /// Anlık toplam CPU kullanimini yuzde olarak dondurur.
    func measureCPUUsage() -> Double {
        var threadList: thread_act_array_t?
        var threadCount: mach_msg_type_number_t = 0
        let result = task_threads(mach_task_self_, &threadList, &threadCount)
        guard result == KERN_SUCCESS, let threads = threadList else { return 0.0 }

        var totalCPU: Double = 0.0
        for i in 0..<Int(threadCount) {
            var threadInfo = thread_basic_info()
            var threadInfoCount = mach_msg_type_number_t(THREAD_INFO_MAX)
            let infoResult = withUnsafeMutablePointer(to: &threadInfo) {
                $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
                    thread_info(threads[i], thread_flavor_t(THREAD_BASIC_INFO), $0, &threadInfoCount)
                }
            }
            if infoResult == KERN_SUCCESS, threadInfo.flags & TH_FLAGS_IDLE == 0 {
                totalCPU += Double(threadInfo.cpu_usage) / Double(TH_USAGE_SCALE) * 100.0
            }
        }
        vm_deallocate(
            mach_task_self_,
            vm_address_t(UInt(bitPattern: threadList)),
            vm_size_t(threadCount) * vm_size_t(MemoryLayout<thread_t>.stride)
        )
        return totalCPU
    }

    // MARK: - Bellek Kullanimi

    /// Uygulamanin guncel bellek kullanimini MB olarak dondurur.
    func measureMemoryUsage() -> Double {
        var info = mach_task_basic_info()
        var count = mach_msg_type_number_t(MemoryLayout<mach_task_basic_info>.size) / 4
        let result = withUnsafeMutablePointer(to: &info) {
            $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
                task_info(mach_task_self_, task_flavor_t(MACH_TASK_BASIC_INFO), $0, &count)
            }
        }
        guard result == KERN_SUCCESS else { return 0 }
        return Double(info.resident_size) / 1_048_576  // Byte -> MB donusumu
    }

    // MARK: - Sure Olcumu

    /// Bir kod blogunu calistirir ve sure olcer.
    /// - Parameters:
    ///   - label: Olcum etiketi (raporda gorunur)
    ///   - block: Suresi olculecek kod bloku
    func measure(label: String, block: () -> Void) {
        let start = CFAbsoluteTimeGetCurrent()
        block()
        let elapsed = (CFAbsoluteTimeGetCurrent() - start) * 1000  // ms cinsinden

        queue.async(flags: .barrier) {
            self.metrics[label, default: []].append(elapsed)
        }
        print("Performans [\(label)]: \(String(format: "%.2f", elapsed)) ms")
    }

    // MARK: - Rapor

    /// Tum olcumlerin ozetini konsola yazdirir.
    func generateReport() {
        queue.sync {
            print("\n====== PERFORMANS RAPORU ======")
            print("CPU: \(String(format: "%.1f", measureCPUUsage()))%")
            print("Bellek: \(String(format: "%.1f", measureMemoryUsage())) MB")
            for (label, times) in metrics {
                let avg = times.reduce(0, +) / Double(times.count)
                print("  \(label) → Ort: \(String(format: "%.2f", avg)) ms (\(times.count) olcum)")
            }
            print("==============================\n")
        }
    }
}
