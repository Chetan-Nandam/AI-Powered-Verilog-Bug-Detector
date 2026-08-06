module traffic_light(
input clk,
input reset,
output reg [1:0] light
);

always @(posedge clk or posedge reset) begin

if(reset)
light <= 2'b00

else begin

case(light)

2'b00:
light <= 2'b01

2'b01:
light <= 2'b10;

2'b10
light <= 2'b00;

default:
light <= 2'b00;

endcase

end

endmodule