from langchain_core.runnables.base import RunnableSerializable
from few_shot import few_shot_small, few_shot_large, few_shot_fine_tuned
from zero_shot import large_chain, small_chain, fine_tuned_chain
from output_model import EducationRequirementOutput
from parser import parse_input
from output import save_to_markdown

def run_test(chain: RunnableSerializable, test_name: str, input_path: str = './academic_details.json') -> None:
    input = parse_input(input_path)
    correct_items = []
    wrong_items = []
    failed_items = []
    for i, item in enumerate(input):
        try:
            result: EducationRequirementOutput = chain.invoke({"query": item.input})
            if item.output == result:
                correct_items.append((item, result))
            else:
                wrong_items.append((item, result))
            i += 1
            if i % 100 == 0:
                print("generated output:", i)
        except Exception as e:
            failed_items.append(item.input)
            print("failed on output", i, item.input, "|", e)

    save_to_markdown(test_name, wrong_items, correct_items, failed_items)
    print("done with run", test_name)


if __name__ == "__main__":
    run_test(few_shot_small, "Small Few Shot")
    run_test(few_shot_large, "Large Few Shot")
    run_test(few_shot_fine_tuned, "Fine Tuned Few Shot")
    run_test(small_chain, "Small Zero Shot")
    run_test(large_chain, "Large Zero Shot")
    run_test(fine_tuned_chain, "Fine Tuned Zero Shot")

    # run_test(few_shot_chain, "Few Shot Test")
