<div align="center">

<img src="assets/chip-banner.svg" alt="Eluva Sreevenkat - ECE, ASIC design, RTL, verification, FPGA" width="100%"/>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3200&pause=900&color=2EE6A6&center=true&vCenter=true&width=720&lines=ASIC+design%3A+from+RTL+to+GDSII;Designing+RTL+in+Verilog+%26+SystemVerilog;Verifying+with+UVM+testbenches;Building+FPGA+accelerators;From+spec+to+silicon" alt="Typing animation"/>
</a>

<br/>

![ASIC](https://img.shields.io/badge/ASIC%20Design-f59e0b?style=for-the-badge&labelColor=0b1117)
![Verilog](https://img.shields.io/badge/Verilog-2ee6a6?style=for-the-badge&labelColor=0b1117)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-38bdf8?style=for-the-badge&labelColor=0b1117)
![UVM](https://img.shields.io/badge/UVM-a78bfa?style=for-the-badge&labelColor=0b1117)
![Xilinx](https://img.shields.io/badge/Vivado%20%7C%20Vitis%20HLS-ef4444?style=for-the-badge&logo=xilinx&logoColor=white&labelColor=0b1117)
![Python](https://img.shields.io/badge/Python-facc15?style=for-the-badge&logo=python&logoColor=black&labelColor=0b1117)
![Followers](https://img.shields.io/github/followers/sreeveenkat?style=for-the-badge&logo=github&color=2ee6a6&labelColor=0b1117)

</div>

---

## `> about_me`

```verilog
module eluva_sreevenkat (
    input  wire clk,          // runs on curiosity
    input  wire rst_n,
    output reg  [31:0] ideas  // pipelined, with hazard detection
);
    always @(posedge clk or negedge rst_n)
        if (!rst_n) ideas <= 32'd0;
        else        ideas <= ideas + 1;   // always shipping
endmodule
```

- 🔬 **ECE engineer** aiming at **ASIC design**: RTL, microarchitecture, verification and the path down to silicon
- 🧠 Building **processors, FIFOs and ALUs** from scratch, then breaking them with testbenches
- ⚡ Working on **FPGA accelerators** for image and neural-network workloads
- 🧮 Exploring **posit arithmetic** and low-precision MAC units, aimed at both FPGA and ASIC implementation
- 📐 Learning the **RTL-to-GDSII flow**: synthesis, static timing analysis, and power, performance and area (PPA) trade-offs
- 🌱 Learning more **UVM**, constrained-random testing and coverage-driven verification

---

## `> toolchain`

| Domain | Stack |
| :-- | :-- |
| **ASIC design** | ![RTL to GDSII](https://img.shields.io/badge/-RTL%20to%20GDSII-f59e0b?style=flat-square) ![Synthesis](https://img.shields.io/badge/-Synthesis-f59e0b?style=flat-square) ![STA](https://img.shields.io/badge/-Static%20Timing%20Analysis-f59e0b?style=flat-square) ![PPA](https://img.shields.io/badge/-PPA%20Optimization-f59e0b?style=flat-square) |
| **HDL** | ![Verilog](https://img.shields.io/badge/-Verilog-2ee6a6?style=flat-square) ![SystemVerilog](https://img.shields.io/badge/-SystemVerilog-38bdf8?style=flat-square) |
| **Verification** | ![UVM](https://img.shields.io/badge/-UVM-a78bfa?style=flat-square) ![Testbenches](https://img.shields.io/badge/-Self--checking%20TBs-a78bfa?style=flat-square) |
| **FPGA / EDA** | ![Vivado](https://img.shields.io/badge/-Vivado-ef4444?style=flat-square&logo=xilinx&logoColor=white) ![Vitis HLS](https://img.shields.io/badge/-Vitis%20HLS-ef4444?style=flat-square&logo=xilinx&logoColor=white) |
| **Architecture** | ![RISC-V](https://img.shields.io/badge/-RISC--V-f59e0b?style=flat-square&logo=riscv&logoColor=white) ![Pipelining](https://img.shields.io/badge/-5--stage%20pipeline-f59e0b?style=flat-square) |
| **Scripting & tools** | ![Python](https://img.shields.io/badge/-Python-facc15?style=flat-square&logo=python&logoColor=black) ![Linux](https://img.shields.io/badge/-Linux-e5e7eb?style=flat-square&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/-Git-f05032?style=flat-square&logo=git&logoColor=white) ![LaTeX](https://img.shields.io/badge/-LaTeX-008080?style=flat-square&logo=latex&logoColor=white) |

---

## `> featured_projects`

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🖼️ <a href="https://github.com/sreeveenkat/FPGA-Image-Super-Resolution-Accelerator">FPGA Image Super-Resolution Accelerator</a></h3>
      Hardware acceleration of image super-resolution on FPGA.<br/><br/>
      <img src="https://img.shields.io/badge/Python-facc15?style=flat-square&logo=python&logoColor=black"/>
    </td>
    <td width="50%" valign="top">
      <h3>🧪 <a href="https://github.com/sreeveenkat/Sync-FIFO-UVM-Verification">Sync FIFO - UVM Verification</a></h3>
      UVM environment for verifying a synchronous FIFO.<br/><br/>
      <img src="https://img.shields.io/badge/SystemVerilog-38bdf8?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🧠 <a href="https://github.com/sreeveenkat/risc-v">RV32I 5-Stage Pipelined CPU</a></h3>
      32-bit RISC-V (RV32I) pipelined processor in Verilog with hazard detection and forwarding.<br/><br/>
      <img src="https://img.shields.io/badge/Verilog-2ee6a6?style=flat-square"/>
    </td>
    <td width="50%" valign="top">
      <h3>🔁 <a href="https://github.com/sreeveenkat/fifo">Sync &amp; Async FIFO</a></h3>
      Parameterizable RTL FIFOs with Gray-code pointer synchronization, checked with a Verilog testbench.<br/><br/>
      <img src="https://img.shields.io/badge/Verilog-2ee6a6?style=flat-square"/>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🛡️ <a href="https://github.com/sreeveenkat/Fault-Tolerant-ALU-16bit">Fault-Tolerant 16-bit ALU</a></h3>
      16-bit ALU designed with fault tolerance in mind.<br/><br/>
      <img src="https://img.shields.io/badge/Verilog-2ee6a6?style=flat-square"/>
    </td>
    <td width="50%" valign="top">
      <h3>⚙️ <a href="https://github.com/sreeveenkat/CPU-32-Bit">32-bit CPU</a></h3>
      A 32-bit CPU core written in Verilog.<br/><br/>
      <img src="https://img.shields.io/badge/Verilog-2ee6a6?style=flat-square"/>
    </td>
  </tr>
</table>

---

## `> design_flow`

How I take an idea from spec to a working FPGA design or an ASIC layout:

```mermaid
flowchart LR
    A([Spec]) --> B[RTL<br/>Verilog / SV]
    B --> C{Simulate<br/>and verify}
    C -- bugs --> B
    C -- coverage met --> D[Synthesis]
    D --> E1[FPGA<br/>P&R + timing]
    E1 --> F1([Bitstream])
    D --> E2[ASIC<br/>floorplan, P&R, STA]
    E2 --> F2([GDSII])

    style A fill:#0b1117,stroke:#2ee6a6,color:#fff
    style B fill:#0b1117,stroke:#38bdf8,color:#fff
    style C fill:#0b1117,stroke:#a78bfa,color:#fff
    style D fill:#0b1117,stroke:#38bdf8,color:#fff
    style E1 fill:#0b1117,stroke:#38bdf8,color:#fff
    style E2 fill:#0b1117,stroke:#f59e0b,color:#fff
    style F1 fill:#0b1117,stroke:#2ee6a6,color:#fff
    style F2 fill:#0b1117,stroke:#f59e0b,color:#fff
```

---

## `> github_stats`

<div align="center">

<img src="assets/stats.svg" alt="GitHub stats" height="200"/>
<img src="assets/languages.svg" alt="Top languages" height="200"/>

</div>

---

## `> connect`

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-sreeveenkat-0b1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sreeveenkat)

<img src="assets/trace-divider.svg" alt="circuit trace divider" width="100%"/>

<sub><code>// open to collaborating on ASIC, RTL, verification and FPGA projects</code></sub>

</div>
