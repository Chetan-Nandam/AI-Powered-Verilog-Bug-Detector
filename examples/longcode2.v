module vending_machine(
    input clk,
    input reset,
    input coin5,
    input coin10,
    output reg dispense,
    output reg [3:0] balance
);

reg [1:0] state;

parameter IDLE = 2'b00;
parameter FIVE = 2'b01;
parameter TEN = 2'b10;
parameter DISPENSE = 2'b11;

always @(posedge clk or posedge reset) begin

    if(reset) begin
        state <= IDLE;
        balance <= 0;
        dispense <= 0;
    end

    else begin

        case(state)

        IDLE:
        begin
            dispense <= 0;

            if(coin5)
            begin
                state <= FIVE
                balance <= 5;
            end

            else if(coin10)
            begin
                state <= TEN;
                balance <= 10
            end
        end

        FIVE:
        begin

            if(coin5)
            begin
                state <= TEN;
                balance <= 10;
            end

            else if(coin10)
            begin
                state <= DISPENSE;
                balance <= 15;
            end

        end

        TEN
        begin

            if(coin5)
            begin
                state <= DISPENSE;
                balance <= 15;
            end

            else if(coin10)
            begin
                state <= DISPENSE;
                balance <= 20;
            end

        end

        DISPENSE:
        begin
            dispense <= 1;
            balance <= 0;
            state <= IDLE;
        end

        default:
        begin
            state <= IDLE;
        end

        endcase

    end

endmodule